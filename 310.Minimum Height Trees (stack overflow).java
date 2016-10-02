/**
 *Result:
 * java.lang.StackOverflowError
 *Date:
 * 10/2/2016
 */
public class Solution {
    class RoadLabel{
        int dest = -1;   //destination
        int dist = -1;   //distance to destination
        public RoadLabel(int dest, int dist){
            this.dest = dest;
            this.dist = dist;
        }
        public boolean isSet(){
            return dest!=-1 || dist!=-1;
        }
        public void set(int dest, int dist){
            this.dest = dest;
            this.dist = dist;
        }
    }
    class Tree{
        int size;
        ArrayList<Node> nodes;
        ArrayList<Integer> roots;
        int[] hashRoot;
        
        class Node{
            int name;
            LinkedList<Integer> adjLst;
            public Node(int name){
                this.name = name;
                adjLst = new LinkedList<Integer>();
            }
            public void addAdj(int adj){
                adjLst.add(adj);
            }
        }
        
        public Tree(int size,int[][] edges){
            this.nodes = new ArrayList<Node>(size);
            this.size = size;
            for(int i=0;i<size;i++){
                nodes.add(new Node(i));
            }
            addEdges(edges);
            findRoots(size,edges);
        }
        private void addEdge(int u, int v){
            nodes.get(u).addAdj(v);
            nodes.get(v).addAdj(u);
        }
        
        private void addEdges(int[][] edges){
            for(int[] edge : edges){
                addEdge(edge[0],edge[1]);
            }
        }
        private void findRoots(int size, int[][] edges){
            roots = new ArrayList<Integer>();
            hashRoot = new int[size];
            for(int[] edge : edges){
                hashRoot[edge[0]]++;
                hashRoot[edge[1]]++;
            }
            for(int i=0;i<size;i++){
                if(hashRoot[i]==1){
                    roots.add(i);
                }
            }
        }
    }
    
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if(n==0){
            return (List<Integer>)(new ArrayList<Integer>(0));
        }
        if(n==1){
            List<Integer> rtn =  new ArrayList<Integer>(1);
            rtn.add(0);
            return rtn;
        }
        RoadLabel[] farthest = new RoadLabel[n];
        RoadLabel[] farther = new RoadLabel[n];
        for(int i=0;i<n;i++){
            farthest[i] = new RoadLabel(-1,-1);
            farther[i] = new RoadLabel(-1,-1);
        }
        
        Tree tree = new Tree(n,edges);
        for(int root : tree.roots){
            farthest[root].set(-1,0);
        }
        farthest[tree.roots.get(0)].set(-1, -1);
        dfs(tree,farthest, farther, tree.roots.get(0),-1,0);
        return findMinHeightRoot(farthest,farther);
    }
    
    private List<Integer> findMinHeightRoot(RoadLabel[] farthest, RoadLabel[] farther){
        List<Integer> res = new LinkedList<>();
        int min = Integer.MAX_VALUE;
        for(int i=0;i<farthest.length;i++){
            int len = farthest[i].dist;
            min = min>len?len:min;
        }
        for(int i=0;i<farthest.length;i++){
        	int len = farthest[i].dist;
            if(min==len)
                res.add(i);
        }
        return res;
    }
    private int dfs(Tree tree, RoadLabel[] farthest, RoadLabel[] farther, int nodeid, int from, int depth){
        RoadLabel newlabel = new RoadLabel(from, depth);
        boolean broadCast = updateRoadLabel(nodeid, farthest, farther, newlabel);
        while(broadCast){
            //the while loop executes at most twice.
            broadCast = false;
            for(int adj : tree.nodes.get(nodeid).adjLst){
                if(adj==from)
                    continue;
                int dist = -1;
                if(farthest[nodeid].dest==adj){
                    dist = dfs(tree,farthest,farther,adj,nodeid,farther[nodeid].dist+1);
                }else{
                    dist = dfs(tree,farthest,farther,adj,nodeid,farthest[nodeid].dist+1);
                }
                broadCast |= updateRoadLabel(nodeid, farthest, farther, new RoadLabel(adj,dist));
            }
        };
        return (farthest[nodeid].dest!=from?farthest[nodeid].dist:farther[nodeid].dist)+1;
    }
    
    /**
     * @return whether a change is made
     */
    private boolean updateRoadLabel(int nodeid, RoadLabel[] farthest, RoadLabel[] farther, RoadLabel curr){
    	if((curr.dist==farthest[nodeid].dist && curr.dest==farthest[nodeid].dest)||(curr.dist==farther[nodeid].dist && curr.dest==farther[nodeid].dest)){
    		return false;
    	}
    	if(farthest[nodeid].dest==curr.dest || farther[nodeid].dest==curr.dest){
    		if(farthest[nodeid].dest==curr.dest){
    			farthest[nodeid]=curr;
    		}else{
    			farther[nodeid]=curr;
    		    if(farthest[nodeid].dist<farther[nodeid].dist){
                	RoadLabel tmp = farther[nodeid];
                    farther[nodeid] = farthest[nodeid];
                    farthest[nodeid] = tmp;
                }
    		}
    		return true;
    	}
        if(!farthest[nodeid].isSet()){
            farthest[nodeid] = curr;
            return true;
        }else if(!farther[nodeid].isSet()){
            farther[nodeid] = curr;
            if(farthest[nodeid].dist<farther[nodeid].dist){
            	RoadLabel tmp = farther[nodeid];
                farther[nodeid] = farthest[nodeid];
                farthest[nodeid] = tmp;
            }
            return true;
        }else{
            if(curr.dist>farther[nodeid].dist){
                farther[nodeid] = curr;
                if(farther[nodeid].dist>farthest[nodeid].dist){
                    RoadLabel tmp = farther[nodeid];
                    farther[nodeid] = farthest[nodeid];
                    farthest[nodeid] = tmp;
                }
                return true;
            }
            return false;
        }
    }
}
