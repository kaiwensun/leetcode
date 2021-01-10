### C

<p>Compiled with <code>gcc 8.2</code> using the gnu99 standard.</p>

<p>Your code is compiled with level one optimization (<code>-O1</code>). <a href="https://github.com/google/sanitizers/wiki/AddressSanitizer" target="_blank">AddressSanitizer</a> is also enabled to help detect out-of-bounds and use-after-free bugs.</p>

<p>Most standard library headers are already included automatically for your convenience.</p>

<p>For hash table operations, you may use <a href="https://troydhanson.github.io/uthash/" target="_blank">uthash</a>. "uthash.h" is included by default. Below are some examples:</p>

<p><b>1. Adding an item to a hash.</b>
<pre>
struct hash_entry {
    int id;            /* we'll use this field as the key */
    char name[10];
    UT_hash_handle hh; /* makes this structure hashable */
};

struct hash_entry *users = NULL;

void add_user(struct hash_entry *s) {
    HASH_ADD_INT(users, id, s);
}
</pre>
</p>

<p><b>2. Looking up an item in a hash:</b>
<pre>
struct hash_entry *find_user(int user_id) {
    struct hash_entry *s;
    HASH_FIND_INT(users, &user_id, s);
    return s;
}
</pre>
</p>

<p><b>3. Deleting an item in a hash:</b>
<pre>
void delete_user(struct hash_entry *user) {
    HASH_DEL(users, user);  
}
</pre>
</p>

### C++

<p>Compiled with <code> clang 11 </code> using the latest C++ 17 standard.</p>

<p>Your code is compiled with level one optimization (<code>-O1</code>). <a href="https://github.com/google/sanitizers/wiki/AddressSanitizer" target="_blank">AddressSanitizer</a> is also enabled to help detect out-of-bounds and use-after-free bugs.</p>

<p>Most standard library headers are already included automatically for your convenience.</p>

### C#

<p><a href="https://docs.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-8" target="_blank">C# 8.0 </a></p>

<p>Your code is compiled with debug flag enabled (<code>/debug</code>).</p>

### Go

<p><code>Go 1.13</code>.</p>

### Java

<p><code>Java SE 13</code>.</p>

<p>Most standard library headers are already included automatically for your convenience.</p>
<p>Includes <code>Pair</code> class from https://docs.oracle.com/javase/8/javafx/api/javafx/util/Pair.html.</p>

### JavaScript

<p><code>Node.js 14.3.0</code>.</p>

<p>Your code is run with <code>--harmony</code> flag, enabling <a href="http://node.green/" target="_blank">new ES6 features</a>.</p>

<p><a href="https://lodash.com" target="_blank">lodash.js</a> library is included by default.</p>

<p>For Priority Queue / Queue data structures, you may use <a href="https://github.com/datastructures-js/priority-queue" target="_blank">datastructures-js/priority-queue</a> and <a href="https://github.com/datastructures-js/queue" target="_blank">datastructures-js/queue</a>.</p>

### Kotlin

<p><code>Kotlin 1.3.10</code>.</p>

### PHP

<p><code>PHP 7.2</code>.</p>
<p>With bcmath module</p>

### Python

<p><code>Python 2.7.12</code>.</p>

<p>Most libraries are already imported automatically for your convenience, such as <a href="https://docs.python.org/2/library/array.html" target="_blank">array</a>, <a href="https://docs.python.org/2/library/bisect.html" target="_blank">bisect</a>, <a href="https://docs.python.org/2/library/collections.html" target="_blank">collections</a>. If you need more libraries, you can import it yourself.</p>

<p>For Map/TreeMap data structure, you may use <a href="http://www.grantjenks.com/docs/sortedcontainers/" target="_blank">sortedcontainers</a> library.</p>

<p>Note that Python 2.7 <a href="https://www.python.org/dev/peps/pep-0373/" target="_blank">will not be maintained past 2020</a>. For the latest Python, please choose Python3 instead.</p>

### Python3

<p><code>Python 3.9</code>.</p>

<p>Most libraries are already imported automatically for your convenience, such as <a href="https://docs.python.org/3/library/array.html" target="_blank">array</a>, <a href="https://docs.python.org/3/library/bisect.html" target="_blank">bisect</a>, <a href="https://docs.python.org/3/library/collections.html" target="_blank">collections</a>. If you need more libraries, you can import it yourself.</p>

<p>For Map/TreeMap data structure, you may use <a href="http://www.grantjenks.com/docs/sortedcontainers/" target="_blank">sortedcontainers</a> library.</p>

### Ruby

<p><code>Ruby 2.7.1</code></p>

<p>Some common data structure implementations are provided in the Algorithms module: https://www.rubydoc.info/github/kanwei/algorithms/Algorithms</p>

### Rust

<p><code>Rust 1.40.0</code></p>

<p>Supports <a href="https://crates.io/crates/rand" target="_blank">rand</a> from crates.io</p>

### Scala

<p><code>Scala 2.13</code>.</p>

### Swift

<p><code>Swift 5.2.5</code>.</p>

### Typescript

<p><code>Node.js 14.3.0</code>.</p>

<p>Your code is run with <code>--harmony</code> flag, enabling <a href="http://node.green/" target="_blank">new ES6 features</a>.</p>

<p><a href="https://lodash.com" target="_blank">lodash.js</a> library is included by default.</p>

