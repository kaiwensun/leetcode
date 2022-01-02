function findAllRecipes(recipes: string[], ingredients: string[][], supplies: string[]): string[] {
    const graph = {};
    for (let i in recipes) {
        graph[recipes[i]] = ingredients[i];
    }
    const supplies_set = new Set(supplies);
    const cooking = new Set();
    function dfs(node: string) {
        if (supplies_set.has(node)) {
            return true;
        }
        if (cooking.has(node) || !graph[node]) {
            return false;
        }
        cooking.add(node);
        for (let ingredient of graph[node]) {
            if (!dfs(ingredient)) {
                cooking.delete(node);
                return false;
            }
        }
        cooking.delete(node);
        supplies_set.add(node);
        return true;
    }
    return recipes.filter(recipe => dfs(recipe));
};

