#include <stdlib.h>

typedef struct  s_node
{
    int *content;
    struct s_node *prev_next;
}               t_node;