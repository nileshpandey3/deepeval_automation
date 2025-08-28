### Demo Test Automation Project using DeepEval and local gemma3 ollama model


### How to Run
- Download and install Ollama https://ollama.com/download
- Pull the gemma3 model (lightweight)
- Make sure its running on your machine 
- `deepeval set-ollama gemma3:1b`
- `pytest tests/ -s`