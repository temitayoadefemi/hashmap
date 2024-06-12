#include <stdio.h>     // Standard input/output library (for printf, etc.)
#include <stdlib.h>    // Standard library (for malloc, free, etc.)

// Define a structure to represent a single node in a linked list
typedef struct ListNode {
    int key;             // The key to store in the hash map
    int value;           // The value associated with the key
    struct ListNode *next; // Pointer to the next node in the linked list (if any)
} ListNode;

// Define a structure to represent the hash map itself
typedef struct HashMap {
    ListNode **buckets; // Array of pointers to linked lists (the buckets)
    int size;          // The number of buckets in the hash map
} HashMap;
