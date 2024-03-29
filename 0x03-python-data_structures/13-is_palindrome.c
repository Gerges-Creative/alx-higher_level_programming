#include "lists.h"

/**
 * is_palindrome - a function that checks if a singly linked list is
 * a palindrome.
 * @head: pointer that points to the head of the singly linked list.
 * Return: 1 if it is a palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *node;
	int *array, n = 0, i;

	if (*head == NULL)
		return (1);
	if (head == NULL)
		return (0);
	node = *head;
	/* while loop to count how many nodes in the linked list */
	while (node != NULL)
	{
		node = node->next;
		n++;
	}

	array = malloc(n * sizeof(int));
	if (array == NULL)
		return (2);
	node = *head;
	for (i = 0; i < n; i++)
	{
		array[i] = node->n;
		node = node->next;
	}

	if (n == 1)
		return (1);
	for (i = 0; i < (n / 2); i++)
	{
		if (array[i] != array[n - i -1])
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}
