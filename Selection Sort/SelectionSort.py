'''
--------------------------------------------------------------
                Sorted array using selection sort
--------------------------------------------------------------
'''
def selectionSort(arr_name):

    # this is the minimum value of that array we assume
    min = arr_name[0];

    # this is the minimum value index number at this moment
    current_index = 0;


    for i in range( len(arr_name)-1 ):

        for j in range(i,len(arr_name) ):

            # true--->if we find any arr_name[j] that is minimum than min
            if min >= arr_name[j]:
                # recording min and its index
                min = arr_name[j];
                current_index = j;

        # swap the minimum element with the first element
        temp = arr_name[i];
        arr_name[i] = min;
        arr_name[current_index] = temp;
        # -----------------------------------------------

        current_index = i;
        min = arr_name[i+1];



ara = [20, 21, 56, 30, 12, 50, 15, 5, 53];

selectionSort(ara);

print(ara);