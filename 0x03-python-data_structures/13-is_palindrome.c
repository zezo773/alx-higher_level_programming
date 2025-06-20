#include "lists.h"
/**
 * reverse - Reverses a singly linked list
 * @head: Pointer to the first node of the list
 *
 * Return: Pointer to the new head (reversed list)
 */
listint_t *reverse(listint_t *head)
{
	listint_t *prv = NULL;
	listint_t *cur = head;
	listint_t *next = NULL;

	while(cur)
	{
		next = cur->next;
		cur->next = prv;
		prv = cur;
		cur = next;
	}
	return (prv);
}
/**
 * isEqual - Compares two singly linked lists
 * @n1: Pointer to the first node of the first list
 * @n2: Pointer to the first node of the second list
 *
 * Return: 1 if both lists are equal, 0 otherwise
 */
int isEqual(listint_t *n1, listint_t *n2)
{
	while(n1 && n2)
	{
		if (n1->n != n2->n)
			return (0);
		n1 = n1->next;
		n2 = n2->next;
	}
	return (1);
}
/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Double pointer to the head of the list
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (!*head || !(*head)->next)
		return (1);

	listint_t *fast = *head, *slow = *head;
	while (fast->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	listint_t *head2;
	head2 = reverse(slow->next);
	slow->next = NULL;

	int ret = isEqual(*head, head2);

	head2 = reverse(head2);
	slow->next = head2;

	return ret;
}
