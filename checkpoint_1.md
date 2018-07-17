
What is the time complexity of the following code? Linear with respect to n, assuming arr is not known.

```
int j = 0;
for(i = 0; i < n; ++i) {
    while(j < n && arr[i] < arr[j]) {
        j++;
    }
}
```

        
