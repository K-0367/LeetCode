class Solution:
    def braceExpansionII(self, expression):
        
        def union(A, B):
            return A | B
        
        def product(A, B):
            result = set()
            for a in A:
                for b in B:
                    result.add(a + b)
            return result
        
        def parse_expr(i):
            # Parse an expression involving unions
            result, i = parse_term(i)
            
            while i < len(expression) and expression[i] == ',':
                next_result, i = parse_term(i + 1)
                result = union(result, next_result)
            
            return result, i
        
        def parse_term(i):
            # Parse concatenated expressions
            result = {""}
            
            while i < len(expression) and expression[i] not in "},":
                
                if expression[i] == '{':
                    current, i = parse_expr(i + 1)
                    
                    # Skip '}'
                    i += 1
                else:
                    current = {expression[i]}
                    i += 1
                
                result = product(result, current)
            
            return result, i
        
        result, _ = parse_expr(0)
        return sorted(result)