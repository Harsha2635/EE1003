#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to calculate probabilities
void simulate_coin_toss(int n, double *probabilities, double *cdf) {
    int outcomes[4] = {0}; // Counts for 0, 1, 2, 3 tails
    int i;

    // Simulate the trials
    for (i = 0; i < n; i++) {
        int tail_count = 0;
        for (int toss = 0; toss < 3; toss++) {
            if (rand() % 2 == 0) { // Random 0 or 1; 0 represents tail
                tail_count++;
            }
        }
        outcomes[tail_count]++;
    }

    // Calculate probabilities
    for (i = 0; i < 4; i++) {
        probabilities[i] = (double)outcomes[i] / n;
    }

    // Calculate CDF
    cdf[0] = probabilities[0];
    for (i = 1; i < 4; i++) {
        cdf[i] = cdf[i - 1] + probabilities[i];
    }
}

// Expose to Python
__attribute__((visibility("default"))) __attribute__((used))
void calculate_probabilities(int n, double *probabilities, double *cdf) {
    srand(time(NULL));
    simulate_coin_toss(n, probabilities, cdf);
}

