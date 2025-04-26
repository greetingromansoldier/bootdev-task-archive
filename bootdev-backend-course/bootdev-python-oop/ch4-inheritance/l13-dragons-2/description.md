# Dragon Fight

We've created a lot of classes in this course—now let's write some code that **uses** them.

---

## Assignment

In the `main()` function, complete the bottom half of the code using **two for-loops**:

1. **First For-Loop**
   - Call `describe()` on each dragon in the same order as the original list.

2. **Second For-Loop**
   - Have **each** dragon use `breathe_fire` at coordinate `(3, 3)`.
   - Pass **all the other dragons** (not the one breathing fire) as the `units` parameter, so we can see which ones get hit by the fire.

Make sure you pass the dragons in the same order as the original list. For example, when **Blue Dragon** breathes fire, it should breathe on the others in this order:

1. Green Dragon
2. Red Dragon
3. Black Dragon

---

## Example Output

After describing the dragons, you might see:

Once you describe the dragons, your output should look like this:
```
Green Dragon is at 0/0
Red Dragon is at 2/2
Blue Dragon is at 4/3
Black Dragon is at 5/-1
```

The output of the first dragon breathing fire should look like this:

```
Green Dragon breathes fire at 3/3 with range 1
====================================
Red Dragon is hit by the fire
Blue Dragon is hit by the fire
Red Dragon breathes fire at 3/3 with range 2
```
Tips
Copying a List

To get a new copy of a list, use the copy() method. If you don't, your new variable will just be a reference to the original list.

```python
nums = [4, 3, 2, 1]
nums_copy = nums.copy()
# nums_copy is [4, 3, 2, 1]
```
Delete from a List
```python
nums = [4, 3, 2, 1]
del nums[1]
# nums is [4, 2, 1]
```
