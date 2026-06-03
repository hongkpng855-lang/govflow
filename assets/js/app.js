/* GovFlow - Alpine.js Application */

document.addEventListener('alpine:init', () => {
  // ─── Process Store ───────────────────────────────────
  Alpine.store('process', {
    data: null,
    currentStep: 1,
    totalSteps: 7,
    freeSteps: 2,
    isLoading: true,
    error: null,

    async load(processId) {
      this.isLoading = true;
      this.error = null;
      try {
        const resp = await fetch('/processes.json');
        if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
        const json = await resp.json();
        this.data = json;
        this.totalSteps = json.totalSteps;
        this.freeSteps = json.freeSteps;
      } catch (err) {
        this.error = '無法載入內容，請重新整理頁面';
        console.error('Load process error:', err);
      } finally {
        this.isLoading = false;
      }
    },

    get steps() {
      return this.data?.steps || [];
    },

    get currentStepData() {
      return this.steps.find(s => s.stepNumber === this.currentStep) || null;
    },

    get isPaid() {
      // Check if user has unlocked (via localStorage)
      return localStorage.getItem('govflow_unlocked') === 'true';
    },

    get unlockedSteps() {
      return this.steps.filter(s => s.isFree || this.isPaid);
    },

    isStepAccessible(stepNum) {
      return stepNum <= this.freeSteps || this.isPaid;
    },

    goToStep(stepNum) {
      if (stepNum >= 1 && stepNum <= this.totalSteps) {
        this.currentStep = stepNum;
        // Scroll to content
        document.getElementById('step-content')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    },

    unlockAll() {
      localStorage.setItem('govflow_unlocked', 'true');
    }
  });

  // ─── Document Overlay ────────────────────────────────
  Alpine.data('docOverlay', () => ({
    open: false,
    doc: null,

    show(doc) {
      this.doc = doc;
      this.open = true;
      document.body.style.overflow = 'hidden';
    },

    close() {
      this.open = false;
      this.doc = null;
      document.body.style.overflow = '';
    }
  }));

  // ─── Payment Link ────────────────────────────────────
  Alpine.data('payment', () => ({
    price: 149,
    currency: 'HKD',

    get displayPrice() {
      return `HK$${this.price}`;
    },

    checkout() {
      window.open('https://1714457598663.gumroad.com/l/wkjykk', '_blank');
    }
  }));

  // ─── Smooth Scroll for Anchor Links ──────────────────
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      if (href === '#') return;
      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });
});
