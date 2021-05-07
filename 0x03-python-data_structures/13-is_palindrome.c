#include "lists.h"

/**
 * _reverse - this function reverse a linked list
 * @temp_hold: pointer to head of list
 * Return: the inverted linked list
 */
listint_t *_reverse(listint_t *temp_hold)
{
	listint_t *temp_1 = NULL, *temp_2 = NULL;

	while (temp_hold != NULL)
	{
		temp_1 = temp_hold->next;
		temp_hold->next = temp_2;
		temp_2 = temp_hold;
		temp_hold = temp_1;
	}
	temp_hold = temp_2;
	return (temp_hold);
}

/**
 * is_palindrome- This function verifies if a linked list is palindrome or not
 * @head: pointer to head of list
 * Return: 1, if the linked list is palindrome and 0, if not is
 */
int is_palindrome(listint_t **head)
{
	/* statament of the variable to the struct */
	listint_t *temp_slow, *temp_slow_2 = NULL, *temp_fast,
		*temp_hold = NULL, *temp_3 = NULL;
	if (head == NULL)
		return ('\0');
	temp_slow = *head, temp_fast = (*head)->next;
	/* loop to determine the midpoint of the list */
	while (temp_fast != NULL)
	{
		/* condicition to when the linked list is pair */
		if (temp_fast->next == NULL)
			break;
		temp_slow = temp_slow->next;
		temp_fast = temp_fast->next->next;
	}
	temp_hold = temp_slow->next;
	temp_slow->next = NULL;
	temp_fast = NULL;
	/* we invoke this function to invest the second half of the list */
	temp_3 = _reverse(temp_hold);
	temp_hold = temp_3;
	temp_slow_2 = *head;
	/* loop to compare the two list */
	while (temp_slow_2 && temp_3)
	{
		/* condicition to comparar the elements of each node */
		if (temp_slow_2->n != temp_3->n)
		{
			temp_slow->next = temp_hold, temp_hold = NULL;
			return (0);
		}
		temp_slow_2 = temp_slow_2->next;
		temp_3 = temp_3->next;
	}
	/* join the two halves */
	temp_slow->next = temp_hold;
	temp_hold = NULL;
	return (1);
}
