#include <stdio.h>  // Standard Input/Output for functions like printf and fprintf
#include <stdlib.h> // General utilities like malloc and exit
#include "hashmap_structs.h" // Assume this file contains the definitions of HashMap and ListNode

// Function to initialize an empty hash map
void initHashMap(HashMap *map, int size) {
    map->size = size;      // Set the initial size of the hash table
    map->buckets = malloc(sizeof(ListNode*) * size); // Allocate memory for the buckets array
    
    // Error handling: check if memory allocation was successful
    if (map->buckets == NULL) {
        fprintf(stderr, "Memory allocation failed\n");  // Print error message to stderr
        exit(1);    // Exit the program with a non-zero status to indicate failure
    }

    // Initialize each bucket to NULL (empty)
    for (int i = 0; i < size; i++) {
        map->buckets[i] = NULL;
    }
}


// Hash function to calculate the index for a given key
int hash(int key, int size) {
    return key % size;  // Simple modulo hash for demonstration 
}

// Function to insert or update a key-value pair in the hash map
void put(HashMap *map, int key, int value) {
    int index = hash(key, map->size);
    ListNode *node = map->buckets[index];

    // Check if the key already exists in the hash table
    while (node != NULL) {
        if (node->key == key) {
            node->value = value; // Update the value if the key exists
            return;
        }
        node = node->next;
    }

    // Key not found, create a new node to store the key-value pair
    ListNode *newNode = malloc(sizeof(ListNode));
    
    // Error handling for memory allocation
    if (newNode == NULL) {
        fprintf(stderr, "Memory Allocation Failed");
        exit(1);
    }

    newNode->key = key;
    newNode->value = value;
    newNode->next = map->buckets[index]; // Insert at the beginning of the linked list
    map->buckets[index] = newNode;
}

// Function to retrieve the value associated with a key
int *get(HashMap *map, int key) {  // Returns a pointer to the value (allows modification)
    int index = hash(key, map->size);
    ListNode *node = map->buckets[index];

    // Search the linked list at the calculated index
    while (node != NULL) {
        if (node->key == key) {
            return &node->value; // Return the address of the value for direct access
        }
        node = node->next;
    }

    return NULL;  // Key not found
}


// Function to free the memory allocated for the hash map
void freeHashMap(HashMap *map) {
    for (int i = 0; i < map->size; i++) {
        ListNode *current = map->buckets[i];
        while (current != NULL) {
            ListNode *temp = current;
            current = current->next;
            free(temp); // Free each node in the linked list
        }
    }
    free(map->buckets); // Free the buckets array
    map->buckets = NULL; // Prevent dangling pointers
}
