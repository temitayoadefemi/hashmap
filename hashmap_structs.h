
#include <stdio.h>
#include <stdlib.h>

typedef struct ListNode {
    int key;
    int value;
    struct ListNode *next;
} 
ListNode;


typedef struct HashMap {
    ListNode **buckets;
    int size;
} 
HashMap;

