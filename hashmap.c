#include <stdio.h>
#include <stdlib.h>
#include <hashmap_structs.h>


void initHashMap(HashMap *map, int size) {
    map->size = size;
    map->buckets = malloc(sizeof(ListNode*) * size);
    if (map->buckets == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }
    for (int i = 0; i < size; i++) {
        map->buckets[i] = NULL;
    }
}


int hash(int key, int size) {
    return key % size;
}


void put(HashMap *map, int key, int value) {
    int index = hash(key, map->size);
    ListNode *node = map->buckets[index];

    // Update the value if the key already exists
    while (node != NULL) {
        if (node->key == key) {
            node->value = value;
            return;
        }
        node = node->next;
    }

    // Key not found, add new node
    ListNode *newNode = malloc(sizeof(ListNode));
    if (newNode == NULL) {
        fprintf(stderr, "Memory Allocation Failed");
        exit(1);
    }

    newNode->key = key;
    newNode->value = value;
    newNode->next = map->buckets[index];
    map->buckets[index] = newNode;
}


int *get(HashMap *map, int key) {
    int index = hash(key, map->size);
    ListNode *node = map->buckets[index];  // Correct accessing of the buckets array

    while (node != NULL) {
        if (node->key == key) {
            return &node->value;  // Return address of the value
        }
        node = node->next;
    }

    return NULL;  // Return NULL if key is not found
}


void freeHashMap(HashMap *map) {
    for (int i = 0; i < map->size; i++) {
        ListNode *current = map->buckets[i];
        while (current != NULL) {
            ListNode *temp = current;
            current = current->next;
            free(temp);
        }
    }
    free(map->buckets);
    map->buckets = NULL;
}

