#include "lists.h"

/**
 * insert_node - insert node at index nth
 * @head: poiter that points to the head node
 * @number: is the number of the nth index to insert node
 * Return: the address of the new node or NULL if it failes
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp, temp2;
	int i = 0;

	temp = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	while (i < number - 1 && temp != NULL)
	{
		temp = temp->next;
		i++;
	}

	if (temp == NULL)
		return (NULL);

	temp2 = temp->next;
	temp->next = new;
	new->next = temp2;

	return (*new);
}
