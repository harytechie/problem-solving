public class Main{
    public static void main (String [] args){
    int a=27;
    int c=0;
    int pow=1;
    if(a%3==0){
        int temp=a;
        for(int i=0;i<temp;i++){
        pow=pow*3;
        c=c+1;
        if(pow==temp){
            System.out.println(a+" is dev of "+c+" times");
            return;
        }
    }
    System.out.print(a);
    }
    else{
        System.out.println(a+"not dev 3");
    }
    }
}

