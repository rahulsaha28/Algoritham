'''
-------------------------------------------------------------
        creating Link-List
        property-------| head, node
-------------------------------------------------------------
'''

from Project4.Node import Node;

class Linklist(object):

    # constructor
    def __init__(self):
        self.__head = None;



    # insert method
    def insert(self, data):

        if self.__head != None:

            next_node = self.__travell(None);
            next_node.next_node = Node(data);

        else:
            self.__head = Node(data);


    # detete method
    def delete(self, index):

        if index == 0:
            self.__head = self.__head.next_node;

        else:
            next_node = self.__travell(index);
            pre_node = self.__travell(index-1);
            pre_node.next_node = next_node.next_node;

#     traveller
    def __travell(self, index):

        if index == None:
            next_node = self.__head;

            while next_node.next_node != index:
                next_node = next_node.next_node;
            return next_node;

        else:
            if index > self.length()-1 or index < 0:
                print('Out of indeex.');
            else:
                v_index = 0;
                next_node = self.__head;
                while v_index != index:
                    v_index +=1;
                    next_node = next_node.next_node;

                return next_node;




    # find length
    def length(self):

        length = 0;
        if self.__head != None:
            next_node = self.__head;
            while next_node.next_node != None:
                length += 1;
                next_node = next_node.next_node;
            return length+1;

        else:
            return length;

    #  search the element
    def search(self, v_data):

        if self.length() != 0:
            next_node = self.__head;

            while next_node.next_node != None:

                if next_node.data != v_data:
                    next_node = next_node.next_node;
                else:
                    return True

            if next_node.data == v_data:
                return True;

            return False;

        else:
            return False;





