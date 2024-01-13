#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle in it.
 * @list: a pointer to a pointer of a head of a linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	/**
	 * I'm going to use the trotoise/hare algorithm where the tortoise
	 * will go one node at a time and the hare 2 node at a time and
	 * if they ever have the same n value of the linked list then there
	 * is a cycle.
	 */
	listint_t *tortoise, *hare;

	tortoise = list;
	hare = list;

	while (hare != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next;
		hare = hare->next;

		if (hare != NULL && tortoise != NULL && tortoise->n == hare->n)
			return (1);
	}

	return (0);
}
