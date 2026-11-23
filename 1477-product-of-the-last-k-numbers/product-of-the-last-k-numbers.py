class ProductOfNumbers:

    def __init__(self):
        # Initialize with 1 to handle multiplication smoothly
        self.prefix_products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # Reset the list because any product including 0 will be 0
            self.prefix_products = [1]
        else:
            # Multiply the new number by the last running product
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k is greater than or equal to the current length, a 0 occurred 
        # within the last k elements (which triggered a reset)
        if k >= len(self.prefix_products):
            return 0
        
        # Divide the total product by the product before the last k elements
        return self.prefix_products[-1] // self.prefix_products[-1 - k]
