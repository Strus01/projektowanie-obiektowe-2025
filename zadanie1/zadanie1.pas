program BubbleSortRandomArray;

const 
    N = 50;

type 
    MyIntArray_T = array[1..N] of integer; 
    
var 
    array_of_random_numbers: MyIntArray_T;


procedure PrintArray(const arr: MyIntArray_T);
var
  i: integer;
begin
  for i := 1 to N do
    Write(arr[i], ' ');
  Writeln;
end;


procedure GenerateRandomNumbers(var arr: MyIntArray_T);
var 
    i: integer;
begin
    Randomize;
    for i := 1 to N do
        arr[i] := Random(101);
end;


procedure BubbleSort(var arr: MyIntArray_T);
var
    i, j, tmp: integer;
begin
    for i := 2 to N do
    begin
        for j := n downto i do
        begin
        if arr[j-1] > arr[j] then
            begin
                tmp := arr[j-1];
                arr[j-1] := arr[j];
                arr[j] := tmp;
            end;
        end;
    end;
end;


begin
  GenerateRandomNumbers(array_of_random_numbers);
  Writeln('Random numbers:');
  PrintArray(array_of_random_numbers);
  
  BubbleSort(array_of_random_numbers);
  Writeln('Sorted numbers:');
  PrintArray(array_of_random_numbers);
  
  ReadLn;
end.
