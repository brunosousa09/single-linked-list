from time import sleep #Puxei a função 'time' do python para que na execução tivesse um pequeno delay

class Node:

    def __init__(self, data):
        self.data=data  #Função '__init__' atuando como o construtor de um novo nó da lista encadeada simples ou single linked list
        self.next=None

class list_encadeada:

    def __init__(self):
        self.head=None       #Função '__init__' atuando como o contrutor da lista encadeada simples vazia ou empty single linked list  

    def append(self, data):
        
        new_node=Node(data)

        if self.head==None:
            self.head=new_node
            return            #Função 'append' para adicionar um item no final da lista
        momentary=self.head 
        while momentary.next:
            momentary=momentary.next

        momentary.next=new_node
        return
            
    def size(self):
        if self.head == None:
            return 0
        else:
            momentary=self.head
            total = 0          #Função 'size' irá retornar o comprimento da lista

            while momentary:
                total+=1
                momentary=momentary.next
            return total

    def the_list(self):
        node_data=[]
        momentary=self.head
                                #A lista, iniciando como vazia
        while momentary:
            node_data.append(momentary.data)
            momentary = momentary.next
        return node_data

    def get(self, index):
        if index>=self.size() or index<0:
           print("ERROR: 'get' Index out or range!")
           return None
        momentary_idx = 0
        momentary = self.head        #Retornar valor do nó no index
        while momentary != None:
            if momentary_idx == index:
                return momentary.data
            momentary=momentary.next
            momentary_idx += 1    
     
    def search_by_item(self, value):
        if self.head==None:
            print("List has no elements")
            return
        momentary=self.head
        while momentary != None:    #Pesquisar pelo item
            if momentary.data==value:
               print('Item found')
               return True
            momentary=momentary.next
        print('Item not found')
        return False

    def remove_at_start(self):
        if self.head is None:
            print('the list has no elements to delete')
            return                          #Remover elemento no inicio da lista
        self.head = self.head.next

    def remove_at_end(self):
        if self.head is None:
           print('the list has no elements to delete')
           return
        momentary = self.head                 #Remover elemento no final da lista
        while momentary.next.next != None:
            momentary = momentary.next
        momentary.next = None

    def remove_element_by_value(self, value):
        momentary=self.head
        if momentary != None:
            if momentary.data == value:
                self.head = momentary.next
                momentary = None
                return                  #Remover elementos pelo valor
        while momentary != None:
            if momentary.data == value:
                break
            previous=momentary
            momentary=momentary.next

        if momentary == None:
            return

        previous.next = momentary.next
        momentary = None            

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head      #Inserir no começo da lista
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return                       #Inserir no final da lista
        momentary = self.head
        while momentary.next is not None:
            momentary = momentary.next
        momentary.next = new_node    

    def insert_at_index(self, index, data):
        if index ==1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        i = 1 
        momentary = self.head                   #Inserir elementos pelo index
        while i < index-1 and momentary is not None:
            momentary = momentary.next
            i = i + 1
        if momentary is None:
            print("ERROR: Index out of range!")
        else:
            new_node = Node(data)
            new_node.next = momentary.next
            momentary.next = new_node          
    
    def display(self):
        object=self.head

        if object is None:
            print ('your list is empty, put some item')
                                                #Parte de apresentação para o usuário
        while object:
            print(object.data)
            object=object.next
        print('----------------------')

    def reverse(self):
        previous_node=None
        object=self.head
        while object != None:
            next=object.next                   #Função com o intuito de inverter colocar a lista de forma contraria ou inversa  
            object.next=previous_node
            previous_node=object
            object=next
        self.head=previous_node 


my_list = list_encadeada()
my_list.display()

sleep(1)

my_list.append(0)
my_list.append(5)
my_list.append(10)
my_list.append(15)
my_list.append(20)
my_list.append(25)
my_list.append(30)        

my_list.display()

sleep(1)

print('total elements in the list: ' + str(my_list.size()))
print(my_list.the_list())
print('-------------------')

sleep(1)

my_list.reverse()
my_list.display()

sleep(1)

my_list.search_by_item(18)
my_list.search_by_item(20)

sleep(1)

my_list.remove_at_start()
my_list.display()

sleep(1)

my_list.remove_at_end()
my_list.display()

sleep(1)

my_list.insert_at_start(-5)
my_list.display()

sleep(1)

my_list.insert_at_end(35)
my_list.display()

sleep(1)

my_list.remove_element_by_value(25)
my_list.display()

sleep(1)

my_list.insert_at_index(2,15)
my_list.display()