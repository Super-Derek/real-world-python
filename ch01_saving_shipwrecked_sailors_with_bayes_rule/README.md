# Chapter Overview – Saving Shipwrecked Sailors with Bayes’ Rule

In this chapter we build a simple search-and-rescue (SAR) simulation that models the Coast Guard looking for a shipwreck off the fictional coast of Cape Python. The core idea is to use Bayesian probability to decide where to search next, instead of sweeping the ocean blindly. By updating our beliefs after each search pass, we can focus effort on the most promising regions and improve the odds of finding survivors with limited time and resources. :contentReference[oaicite:0]{index=0}

## Goal of the Search and Rescue Model

The model’s goal is to answer a practical question:

> Given limited search time and imperfect detection, how should we allocate search effort across different regions of the ocean to maximize our chance of finding the wreck?

To do that, the simulation:

- Divides the search area into regions (a grid or set of zones)
- Assigns each region an initial probability that the shipwreck is there (the **prior**)
- Simulates search passes with some probability of detection in each region
- Uses the results of those searches to update the probabilities (the **posterior**)
- Repeats the process to see how effective different search strategies are over many trials

## Bayes’ Rule in This Context

Bayes’ Rule lets us update our belief about where the shipwreck is after we search a region and **do not** find it.

Informally:

- Before searching, each region has a prior probability that the ship is there.
- Searching a region does **not** guarantee we find the ship, even if it is there. The search has a **probability of detection (POD)**.
- If a search turns up nothing, that result makes it _less_ likely the ship is in the searched region and _relatively more_ likely it is in the others.
- Bayes’ Rule gives the exact formula for turning “no detection” plus POD into new, normalized probabilities for all regions.

So each time we search, we replace the old probabilities with updated ones that reflect what we have just learned. Over multiple passes, the probability mass gradually shifts away from regions that have been searched thoroughly without success and toward regions that have not been searched or were searched less effectively.

## High-Level Structure of the Simulation

At a high level, the simulation is structured around a loop of:

1. **Initialize the search area**

   - Define a grid or list of regions.
   - Assign prior probabilities to each region so they sum to 1.0.
   - Optionally vary priors to reflect real-world knowledge (shipping lanes, currents, etc.).

2. **Place the target**

   - Randomly choose the true region where the shipwreck actually is.
   - Use a fixed random seed when needed so results can be reproduced.

3. **Simulate a search pass**

   - Choose which region to search next (strategy).
   - Apply a probability of detection for that region.
   - Randomly determine whether the wreck is detected, based on POD and the true location.

4. **Update beliefs with Bayes’ Rule**

   - If the target is found, record success and end the trial.
   - If not found, update the probabilities for all regions using Bayes’ Rule so they still sum to 1.0.

5. **Repeat over many trials**
   - Run many independent simulations.
   - Track statistics: how often the wreck is found, how many search passes are needed, and how different strategies perform.

## Key Concepts and Functions in the Code

The implementation naturally centers around a few concepts and helper functions:

- **Grid / region representation**

  - A way to represent the search area, such as:
    - A list of regions with names and probabilities
    - Or a 2D grid structure for more visual layouts

- **Prior initialization**

  - A function to create the initial probability distribution over regions.
  - Ensures all priors are non-negative and sum to 1.0.

- **Target placement**

  - A function to randomly select the “true” region.
  - Uses `random` with optional seeding for reproducible runs.

- **Search pass simulation**

  - Given a region and POD, simulate whether the target is detected.
  - Handles both “found” and “not found” cases cleanly.

- **Bayesian update**

  - A function that applies Bayes’ Rule to update all region probabilities after an unsuccessful search.
  - Re-normalizes probabilities so they form a valid distribution.

- **Strategy and trial runner**
  - A function or loop that:
    - Chooses the next region to search (e.g., highest probability first).
    - Repeats search and update steps until the target is found or a limit is reached.
  - Another layer to run many trials and collect aggregate statistics.

Later, the chapter uses these pieces to explore different search strategies and visualize results, showing how Bayesian reasoning can yield smarter, data-driven search patterns instead of naive guesswork. :contentReference[oaicite:1]{index=1}
