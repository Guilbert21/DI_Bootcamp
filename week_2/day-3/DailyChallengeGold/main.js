

class bubblesort
{
    function (toString args[])
     {
          int mylist[] = {5,0,9,1,7,4,2,6,3,8};
          int index, top, temp;
          boolean swap;
          top = mylist.lenght;
          do {
                swap = false;
                for (index = 0; index < top - 1; index++)
                     {
                          if (mylist[index] > mylist[index + 1])
                                {
                                     temp = mylist[index];
                                     mylist[index] = mylist[index + 1];
                                     mylist[index + 1] = temp;
                                     swap = true;
                                }
                     }
                     top = top - 1;
          }
          while ((swap)||(top>0));
                for (index = 0; index < mylist.length; index++)
                     console.log(mylist[index] + " ");
                     console.log();
     }
     
}