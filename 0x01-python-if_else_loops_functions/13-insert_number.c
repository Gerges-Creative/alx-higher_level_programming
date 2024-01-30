#include "lists.h"

/**
 * insert_node - insert node at index nth
 * @head: poiter that points to the head node
 * @number: is the number of the nth index to insert node
 * Return: the address of the new node or NULL if it failes
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp, *temp2;
	int i = 0, j = 0;

	temp = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	if (*head == NULL)
	{
		new->n = number;
		new->next = NULL;
		*head = new;
		return (*head);
	}
	else if (number < 0 && temp != NULL)
	{
		new->n = number;
		new->next = *head;
		*head = new;
		return (*head);
	}

	while (number > temp->n && temp->next != NULL)
	{
		temp = temp->next;
		i++;
	}

	temp = *head;

	if (temp->next == NULL)
	{
		temp->next = new;
		new->next = NULL;
		new->n = number;
		return (new);
	}

	while (j < i - 1)
	{
		temp = temp->next;
		j++;
	}

	temp2 = temp->next;
	new->next = temp2;
	new->n = number;
	temp->next = new;

	return (new);
}
