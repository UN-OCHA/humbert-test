docker run  -it --init \
  --user="$(id -u):$(id -g)" \
  --volume="$PWD:/workspace" \
  openai:local python3 testing.py

