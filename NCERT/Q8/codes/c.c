#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to simulate rolling a single die
void roll_one_die(int trials, int *results) {
    srand(time(0));
    for (int i = 0; i < trials; i++) {
        int die = (rand() % 6) + 1; // Generate numbers from 1 to 10
        if (die > 6) {
            results[6]++; // Increment "greater than 6" category
        } else {
            results[die - 1]++; // Increment corresponding die face count
        }
    }
}

