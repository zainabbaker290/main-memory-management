#Author - Zainab Baker 
#Student number - 119340513

#Single Linked List class takes in Block class 
class SingleLinkedList:
    
    def __init__(self):  
        self.head = None
        self.node_list = []
  
  # insertion method for the linked list
    def enqueue_node(self, block):
        new_node = block
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
        self.node_list.append(new_node.element)
    
    #pop off node that has been in queue for longest time
    def dequeue_head(self):
        self.node_list.pop(0)
        deleted_node = self.head
        self.head = self.head.next 
        return deleted_node.element
    
    #first fit algorithm 
    #if process finds block with equal or more pages needed, use that block and pop it off 
    def dequeue_element(self,element):
        try:
            current = self.head
            if (current.element >= element):
                self.head = current.next
                for node in self.node_list:
                    if node == current.element:
                        self.node_list.remove(node)
                print("block holding sum of pages " + str(current.element) + " was selected")
                current = None
                return 
            while(current):
                if current.element >= element:
                    break
                prev = current
                current = current.next

            #if no block can fulfill the process, that means the process is too large 
            if(current == None):
                return "process too large for system"
            
            prev.next = current.next
            for node in self.node_list:
                if node == current.element:
                    self.node_list.remove(node)
            print("block holding sum of pages " + str(current.element) + " was selected")
            current = None
        #if no current blocks are free 
        except:
            return "no current blocks free, wait for block to be free"
        
    #print nodes in form of list 
    def return_nodes(self):
        return self.node_list 
    
    #print how many blocks are free 
    def node_list_size(self):
        return "length of blocks in linked list is " + str(len(self.node_list))

#Page Class 
class Page:
    def __init__(self, id, state):
        self.size = 4 #fixed size of 4KB
        self.id = id
        self.state = state #state to keep track in second chance algorithm 
    
    def get_size(self):
        return self.size
    
    def get_id(self):
        return self.id
    
    def get_state(self):
        return self.state
    
    def set_state(self, state):
        self.state = state 

#Block Class 
class Block:
    def __init__(self,id, block_size,max_pages, pages, element):
        self.id = id 
        self.block_size = block_size
        self.max_pages = max_pages #max num of pages block can hold 
        self.pages = pages #list of pages 
        self.element = element #the accumulated Kb of all pages summed together 
        self.next = None #pointer for SLL 
    
    def get_size(self):
        return self.size
    
    def get_element(self):
        return self.element
    
    #second chance algorithm 
    def second_chance(self):
        for page in self.pages:
            if page.state == 0:
                #page replacement 
                print("page " + str(page.get_id()) + " of block "+ str(self.id) + " is being replaced")
            else:
                page.set_state(0)
        
        page_counter = 0
        for page in self.pages:
            length_list = len(self.pages)
            if page.state == 0:
                page_counter += 1
                if page_counter == length_list:
                    return "All pages free, block " + str(self.id) + " ready for new process"

#Process class 
class Process:
    def __init__(self, id, num_KB_needed):
        self.id = id
        self.num_KB_needed = num_KB_needed #num of KB needed to fulfill process 
    
    def get_num_KB_needed(self):
        return self.num_KB_needed

#creating pages and page lists 
#page lists go into Block using aggregation --> a block has a page list which has all the pages embedded in it
#in list act as FIFO queue 
page_0 = Page(0,0)
page_1 = Page(1,0)

page_list_block_0 = [page_0,page_1]

page_2 = Page(2,0)
page_3 = Page(3,0)

page_list_block_1 = [page_2,page_3]

page_4 = Page(4,0)
page_5 = Page(5,0)
page_6 = Page(6,0)
page_7 = Page(7,0)
page_8 = Page(8,0)
page_9 = Page(9,1)
page_10 = Page(10,0)
page_11 = Page(11,0)
page_12 = Page(12,1)
page_13 = Page(13,0)
page_14 = Page(14,1)
page_15 = Page(15,0)
page_16 = Page(16,1)
page_17 = Page(17,1)
page_18 = Page(18,0)
page_19 = Page(19,0)

page_list_block_2 = [page_4,page_5, page_6, page_7, page_8, page_9, page_10, page_11, page_12, page_13, 
                        page_14, page_15, page_16, page_17, page_18, page_19]

page_20 = Page(20,0)
page_21 = Page(21,0)
page_22 = Page(22,0)
page_23 = Page(23,0)
page_24 = Page(24,0)
page_25= Page(25,0)
page_26 = Page(26,0)
page_27 = Page(27,0)
page_28 = Page(28,0)
page_29 = Page(29,0)
page_30 = Page(30,0)
page_31 = Page(31,0)
page_32 = Page(32,0)
page_33 = Page(33,0)
page_34 = Page(34,0)
page_35 = Page(35,0)
page_36 = Page(36,0)
page_37 = Page(37,0)
page_38 = Page(38,0)
page_39 = Page(39,0)
page_40 = Page(40,0)
page_41 = Page(41,0)
page_42 = Page(42,0)
page_43 = Page(43,0)
page_44 = Page(44,0)
page_45 = Page(45,0)
page_46 = Page(46,0)
page_47 = Page(47,0)
page_48 = Page(48,0)
page_49 = Page(49,0)
page_50 = Page(50,0)
page_51 = Page(51,0)

page_list_block_3 = [page_20,page_21, page_22, page_23, page_24, page_25, page_26, page_27, page_28, page_29, 
                        page_30, page_31, page_32, page_33, page_34, page_35, page_36,page_37, page_38, page_39, 
                        page_40, page_41, page_42, page_43, page_44, page_45, 
                        page_46, page_47, page_48, page_49, page_50, page_51]

page_52 = Page(52,0)
page_53 = Page(53,0)
page_54 = Page(54,0)
page_55 = Page(55,0)
page_56 = Page(56,0)
page_57 = Page(57,0)
page_58 = Page(58,0)
page_59 = Page(59,0)

page_list_block_4 = [page_52,page_53, page_54, page_55, page_56, page_57, page_58, page_59]

block0 = Block(0,32, 2, page_list_block_0, 256)
block1 = Block(1,32, 2, page_list_block_1, 256)
block2 = Block(2,16,16,page_list_block_2, 1024)
block3 = Block(3,16,32,page_list_block_3, 2048)
block4 = Block(4,16,8,page_list_block_4, 512)

process_0= Process(0, 200)
process_1 = Process(1, 600)
process_2 = Process(2,900)
process_3= Process(3, 10000)
process_4 = Process(4,200)
process_5 =Process(5, 300)

#creating SLL with blocks in it 
linked_list_blocks = SingleLinkedList()
linked_list_blocks.enqueue_node(block0)
linked_list_blocks.enqueue_node(block1)
linked_list_blocks.enqueue_node(block2)
linked_list_blocks.enqueue_node(block3)
#printing amount of blocks we start with 
print(linked_list_blocks.return_nodes())

print("showing processes all being allocated until no free memory")
print(linked_list_blocks.dequeue_element(process_0.get_num_KB_needed()))
print(linked_list_blocks.node_list_size())
print(linked_list_blocks.dequeue_element(process_1.get_num_KB_needed()))
print(linked_list_blocks.node_list_size())
print(linked_list_blocks.dequeue_element(process_2.get_num_KB_needed()))
print(linked_list_blocks.node_list_size())
#showing what happens when a process is too big 
print("showing when the process is too big and no block can fulfill its needs")
print(linked_list_blocks.dequeue_element(process_3.get_num_KB_needed()))
print(linked_list_blocks.node_list_size())
print(linked_list_blocks.dequeue_element(process_4.get_num_KB_needed()))
print(linked_list_blocks.node_list_size())
print("showing when all blocks are being used and process is waiting for a block")
print(linked_list_blocks.dequeue_element(process_5.get_num_KB_needed()))
#page replacement 
print("PAGE REPLACEMENT")
print(block2.second_chance())
linked_list_blocks.enqueue_node(block2)
print(linked_list_blocks.dequeue_element(process_5.get_num_KB_needed()))















        



