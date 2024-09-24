#!/bin/bash

# A set of science prompts ranging from physics to biology, space, and more.
declare -a prompts=(
   "Can dark matter interact with ordinary matter, and how might we detect it?"
    "What biological processes contribute to aging, and how can they be slowed?"
    "How do supermassive black holes form at the center of galaxies?"
    "What are the potential impacts of quantum computing on modern cryptography?"
    "How does CRISPR technology allow for precise genetic editing?"
    "What role do neutrinos play in the standard model of particle physics?"
    "How is climate change affecting oceanic currents and marine ecosystems?"
    "In what ways does epigenetics influence gene expression across generations?"
    "How does the expansion of the universe affect distant galaxies over time?"
    "What advancements are being made toward nuclear fusion as a sustainable energy source?"
)

# Iterate through each prompt and send it as a request
for prompt in "${prompts[@]}"
do
    #  Send a POST request to the chatbot's execution endpoint using curl
    curl --location 'http://localhost:5500/execution' \
         --header 'Content-Type: application/json' \
         --data '{
             "text": ["'"$prompt"'"]
         }' &
done

# Wait for all parallel requests to finish before ending the script
wait

echo "All requests have been completed!"