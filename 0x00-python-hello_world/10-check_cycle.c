#include "lists.h"

/**
 * check_cycle - hecks if a singly linked list has a cycle in it.
 * @list: pointer to linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		/* If the pointers meet, then there is a cycle */
		if (slow == fast)
			return (1);
	}

	/* If the loop terminates without finding a cycle, return 0 */
	return (0);
}
