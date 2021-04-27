#include "lists.h"

/**
 *check_cycle - Function that looks if it is a linked list cycle
 *@list: pointer to the struct
 *Return: 1, if the linked list is cycle and 0, if no is.
 */
int check_cycle(listint_t *list)
{
	/* Declaration of the varibles, of type struct */
	listint_t *p_1 = NULL, *p_2 = NULL;

	p_1 = list;
	p_2 = list;

	/* Travel the linked lists */
	while (p_1 && p_2 && p_2->next)
	{
		/*This pointer advances from a node */
		p_1 = p_1->next;
		/*This pointer advances from two nodes */
		p_2 = p_2->next->next;
		/* If the nodes are equal, is linked list cycle */
		if (p_1 == p_2)
			return (1);
	}
	/* No are linked list cycle */
	return (0);
}
