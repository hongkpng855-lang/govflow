"""Quick test: gateway module load test"""
import sys, os
sys.path.insert(0, "C:\\Users\\hongk\\.hermes\\hermes-agent")

# Load the module that causes the issue
print("Loading conversation_loop...")
from agent.conversation_loop import INTERRUPT_WAITING_FOR_MODEL_PREFIX
print("OK - module loaded")
print(INTERRUPT_WAITING_FOR_MODEL_PREFIX[:50])
print("SUCCESS")
