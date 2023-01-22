#include "lists.h"

/**
* check_cycle - function that checks if singly list has a cycle
* @list: pointer to checked list
* Return: 0 on fail, 1 on success
*/

int check_cycle(listint_t *list)
{
	listint_t *temp;

	if (!list)
	{
		return (0);
	}

	while (list)
	{
		temp = list;
		list = list->next;

		if (temp <= list)
		{
			return (1);
		}
	}
	return (0);
}
