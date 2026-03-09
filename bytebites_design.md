+----------------+
|   Customer     |
+----------------+
| - name: String |
| - purchaseHistory: List<Order> |
+----------------+

+----------------+
|   MenuItem     |
+----------------+
| - name: String |
| - price: Float |
| - category: String |
| - popularityRating: Int |
+----------------+

+----------------+
|     Menu       |
+----------------+
| - items: List<MenuItem> |
+----------------+
| + filterByCategory(category: String): List<MenuItem> |
+----------------+

+----------------+
|     Order      |
+----------------+
| - selectedItems: List<MenuItem> |
| - totalCost: Float |
+----------------+