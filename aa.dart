void main() {
  Map<int, int> a = {1: 2, 3: 4};
  for (var k in a.entries){
    print(k.); // prints 1, 3
  }
  print(a.entries.toList());
}
