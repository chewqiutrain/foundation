# TODO: more tests, find property testing package?

from qfoundation.datastructures.SinglyLinkedList import SinglyLinkedList

def getValueAtSLL(sll, index):
	# :param index: index at which to get value
	currNode = sll.headval 
	count = 0 
	while count < index:
		currNode = currNode.next 
		count += 1
	return currNode.val 

def tailInsert():
	# single element tests
	targetVal0 = 0
	s = SinglyLinkedList()
	s.insertAtTail(targetVal0)
	assert(getValueAtSLL(s,0) == targetVal0), \
	"Failed insertAtTail, targetVal0 = {target_val}".format(\
		target_val = targetVal0)


	return True

def headInsert():
	# single element tests
	targetVal0 = 0 
	s = SinglyLinkedList()
	s.insertAtHead(targetVal0)
	assert(getValueAtSLL(s,0) == targetVal0), \
	"Failed insertAtHead, targetVal0 = {target_val}".format(\
		target_val = targetVal0)

	return True 


def main():
	tailInsert()
	headInsert()

main()
