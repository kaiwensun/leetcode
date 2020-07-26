int isNotLast(struct ListNode* node)
{
	return node->next != NULL;
}
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
	int carry = 0;
	struct ListNode* p1, *p2;
	for (p1 = l1, p2 = l2; isNotLast(p1) && isNotLast(p2); p1 = p1->next, p2 = p2->next)
	{
		int digit_sum = p1->val + p2->val + carry;
		carry = digit_sum / 10;
		digit_sum %= 10;
		p1->val = digit_sum;
	}
	if (p1->next==NULL && p2->next == NULL)
	{
		int digit_sum = p1->val + p2->val + carry;
		if (digit_sum >= 10)
		{
			struct ListNode* new_digit = (struct ListNode*)malloc(sizeof(struct ListNode));
			new_digit->val = 1;
			new_digit->next = NULL;
			p1->next = new_digit;
			digit_sum -= 10;
		}
		p1->val = digit_sum;
	}
	else
	{
		int digit_sum = p1->val + p2->val + carry;
		carry = digit_sum / 10;
		digit_sum %= 10;
		p1->val = digit_sum;
		p1->next = p1->next == NULL ? p2->next : p1->next;
		//p1 should never be NULL
		while (carry==1)
		{
			if (p1->next == NULL)
			{
				p1->next = (struct ListNode*)malloc(sizeof(struct ListNode));
				p1->next->val = 1;
				p1->next->next = NULL;
				break;
			}
			int digit_sum = p1->next->val + carry;
			p1->next->val = digit_sum % 10;
			carry = digit_sum / 10;
			p1 = p1->next;
		}
	}
	return l1;
}
struct ListNode* makeList(char* str)
{
	struct ListNode* node = NULL;
	for (char* c = str; *c != '\0'; c++)
	{
		struct ListNode* new_node = (struct ListNode*)malloc(sizeof(struct ListNode));
		new_node->val = *c - '0';
		new_node->next = node;
		node = new_node;
	}
	return node;
}

