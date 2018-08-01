# TEST FROM SCRATCH
import sys
import time

def read_csv(path, separator=','):
    mat = [map(str, line.replace('\n','').split(separator)) for line in open(path, 'r').readlines()]
    return [[row[j] for row in mat] for j in range(len(mat[0]))]

class LectiveEnum(object):
    # 4, 3, 34, 2, 24, 23, 234, 1, 14, 13, 134, 12, 124, 123, 1234
    def __init__(self, n):
        self.n = n
        self.current = None
        self.stack = []
    
    def next(self, current):
        
        # current = copy.copy(crt)
        # if current is None:
        #     current = []
        # NORMALLY, WE'LL TRY TO ADD A NEW ELEMENT N ON THE RIGHT
        # UNLESS THE LAST ELEMENT OF THE CURRENT ENUMERATION IS N
        # 12 -> 124
        if not bool(current) or current[-1] != self.n:
            self.stack.append(self.n)
            current.append(self.n)
        # IF THE THE LAST ELEMENT IS INDEED N, WE'LL TRY TO LOWER IT
        # 14-> 13
        else:
            current[-1] -= 1
            self.stack[-1] = current[-1]
            # IT MAY BE THAT LOWERING IT CAUSES A SIDE EFFECT
            # 134 -> 133
            # IN THIS CASE, WE'LL REMOVE THE LAST ELEMENT AND DECREASE THE SECOND THE LAST ELEMENT
            # NOTICE THAT THIS SHOULD CASCADE UNTIL CONVERGENCE
            # 234 -> 233 -> 22 -> 1
            while len(current) > 1 and current[-1] <= current[-2]:
                #current = current[:-1]
                del current[len(current)-1]
                current[-1] -= 1
                self.stack[-1] = current[-1]
        # if current == [-1]:
        #     return None
        # print len(current)-len(self.stack)
        for i in range(len(self.stack)-len(current)):
            #print self.stack,'pop',
            self.stack.pop()
            self.stack[-1] = current[-1]
            #print self.stack
        return current
    
    def last(self, crt):
        crt.extend(range(crt[-1]+1, self.n+1))
        return crt

    # def next(self):
    #     if self.current is None:
    #         self.current = []
    #     # NORMALLY, WE'LL TRY TO ADD A NEW ELEMENT N ON THE RIGHT
    #     # UNLESS THE LAST ELEMENT OF THE CURRENT ENUMERATION IS N
    #     # 12 -> 124
    #     if not bool(self.current) or self.current[-1] != self.n:
    #         self.current.append(self.n)
    #     # IF THE THE LAST ELEMENT IS INDEED N, WE'LL TRY TO LOWER IT
    #     # 14-> 13
    #     else:
    #         self.current[-1] -= 1 
    #         # IT MAY BE THAT LOWERING IT CAUSES A SIDE EFFECT
    #         # 134 -> 133
    #         # IN THIS CASE, WE'LL REMOVE THE LAST ELEMENT AND DECREASE THE SECOND THE LAST ELEMENT
    #         # NOTICE THAT THIS SHOULD CASCADE UNTIL CONVERGENCE
    #         # 234 -> 233 -> 22 -> 1
    #         while len(self.current) > 1 and self.current[-1] <= self.current[-2]:
    #             self.current = self.current[:-1]
    #             self.current[-1] -= 1
    #     if self.current == [-1]:
    #         self.current = None
    #     return self.current
    def skip_level(self):
        self.current.append(self.current[-1])

    def compare(self, el1, el2):
        return el1.issubset(el2) or tuple(sorted(el2)) < tuple(sorted(el1))

def lst_to_partitions(lst):
    hashes = {}
    #print list(enumerate(lst))
    for i, j in enumerate(lst):
        hashes.setdefault(j, set([])).add(i)
    return sorted([i for i in hashes.values()], key = lambda k: len(k), reverse=True)

def intersection(desc1, desc2):
    '''
    Procedure STRIPPED_PRODUCT defined in [1]
    '''
    new_desc = []
    T = {}
    S = {}
    for i, k in enumerate(desc1):
        for t in k:
            T[t] = i
        S[i] = set([])
    for i, k in enumerate(desc2):
        for t in k:
            if T.get(t, None) is not None:
                S[T[t]].add(t)
        for t in k:
            if T.get(t, None) is not None:
                if len(S[T[t]]) > 1:
                    new_desc.append(S[T[t]])
                S[T[t]] = set([])
    return new_desc    

def pat_leq(desc1, desc2):
    for i in desc1:
        if not any(i.issubset(j) for j in desc2):
            return False
    return True

def l_close(pat, L):
    #print L
    newpat = set(pat)
    
    complement = set([])
    while True:
        subparts = [con for ant, con in L if len(ant) < len(newpat) and ant.issubset(newpat)]
        if bool(subparts):
            complement = reduce(set.union, subparts)
            if complement.issubset(newpat):
                break
            else:
                newpat.update(complement)
        else:
            break
    return newpat

def execute():
    ctx = read_csv(sys.argv[1])
    partitions = [filter(lambda x:len(x)>1, lst_to_partitions(j)) for j in ctx]
    # print [len(i) for i in partitions]
    # ps = {i: j for i, j in enumerate(sorted(partitions, key=lambda k: (len(k), len(k[0])), reverse=False))}
    #sorted_idx_map = {j:i for i, j in enumerate([i[0] for i in sorted(enumerate(partitions), reverse=False, key=lambda (i, k): (len(k), len(k[0])))])}
    #print sorted_idx_map
    
    #ps =  {sorted_idx_map[i]: j for i, j in enumerate(partitions)}
    ps =  {i: j for i, j in enumerate(partitions)}

    atts = range(len(ctx))
    for i in atts:
        print i, len(ps[i])
    L = []
    enum = LectiveEnum(len(atts)-1)
    intent = []
    enum.next(intent)
    iterations = 0
    stack = [([],[])]

    t0 = time.time()
    while intent != [-1]:

        for prevint, prevext in reversed(stack):
            if len(intent) < len(prevint) or any(x not in intent for x in prevint):
                stack.pop()
            else:
                break

        iterations+=1

        print '\r {:<30}'.format(intent),
        sys.stdout.flush()
        preintent = l_close(intent, L)
        s_preintent = sorted(preintent)
        # if not tuple(sorted(intent)) <= tuple(sorted(preintent)):
        if any(i>j for i,j in zip(intent, s_preintent)):# not tuple(sorted(intent)) <= tuple(sorted(preintent)):
            enum.next(enum.last(intent))
            continue
        # WE NEED TO RECOVER THE PREVIOUS EXTENT CALCULATED FOR THE PREFIX 
        # OF INTENT, RECALL THAT intent IS A PREFIX PLUS SOMETHING, AND WE
        # HAVE ALREADY CALCULATED THE EXTENT FOR THE PREFIX. HOWEVER, IT MAY
        # BE THAT AT SOME JUMP LIKE THE PREVIOUS ONE FOR THE PRE-INTENT OR THE 
        # FOLLOWING FOR THE CLOSED SETS, THE INTENT IS A PREFIX, PLUS A SET OF 
        # ATTRIBUTES. THUS, WE FIRSTLY NEED TO KNOW WHAT WAS THE PREVIOUS PREINTENT
        # IN THE THREE FOR WHICH WE CALCULATED AN EXTENT.

        # WE NEED TO CALCULATE THE PRE-EXTENT FOR THE PRE-INTENT
        # THE PREINTENT IS COMPOSED BY AN ENUMERATED INTENT AND A SET OF ATTRIBUTES
        # OBTAINED FROM THE PRECLOSURE.
        # TE INTENT ENUMERATED IS COMPOSED BY A PREFIX AND A

        
        # previous_extent = ext_stack[-1]
        #print '<', intent, previous_extent, '<'
        
        prevint, prevext = stack[-1]
        #print '*'*100
        #print prevint, intent, preintent
        
        #preextent = reduce(intersection, [ps[i] for i in preintent])
        preextent = reduce(intersection, prevext+[ps[i] for i in preintent if i not in prevint])
        stack.append((preintent, [preextent]))
        # ext_stack.append(preextent)
        # ext_stack.append(intent)


        # if not bool(preextent):
        #     enum.next(enum.last(intent))
        #     continue
        
        closed_preintent = set([i for i, j in ps.items() if i not in preintent and pat_leq(preextent, j)])

        if bool(closed_preintent):            
            # print '\t', preintent, closed_preintent
            L.append((preintent, closed_preintent.union(preintent)))
            if max(intent) < min(closed_preintent):
                intent = sorted(closed_preintent.union(preintent))
            else:
                enum.last(intent)
        else:
            intent = sorted(preintent)
        
        enum.next(intent)
    print
    # print L
    print len(L)
    print iterations 
    print 'Time:', time.time()-t0
    for i, j in L:
        print i, j-i
    print 
    #print cache

if __name__ == "__main__":
    execute()