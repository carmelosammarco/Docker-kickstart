<template>
  <!-- eslint-disable -->
  <section>
    <link href="https://fonts.googleapis.com/css?family=Press+Start+2P" rel="stylesheet" />
    <h1>ToDoS</h1>
    <input type="text" class="nes-input" id="todo-input" placeholder="Add ToDo..." size="200" />
    <button class="Add" v-on:click="addTodo">Add todo</button>
    <ul>
      <li v-for="todo in todos" :key="todo.text" class="flex">
        <label>
          <input type="checkbox" class="nes-checkbox" v-on:click="removeTodo(todo._id)" />
          <span>&nbsp</span>
        </label>
        <span>{{ todo.title }}</span>
        <div class="space"></div>
        <!--<button class="nes-btn is-error padding" v-on:click="removeTodo(todo._id)">X</button>-->
        <button class="Add delete" v-on:click="removeTodo(todo._id)">X</button>
      </li>
    </ul>
  </section>
</template>

<script>
import Api from '@/services/Api'

/* eslint-disable */
export default {
  name: "Main",
  data: function() {
    return {
      todos: []
    };
  },
  beforeMount() {
    this.getTodos();
  },
  methods: {
    addTodo: async function() {
      const element = document.getElementById("todo-input");

      Api().post(`todo`, {
        title: element.value
      });
      this.todos.push({ title: element.value });
    },
    removeTodo: function(id) {
      Api().delete(`todo/${id}`, () => {});
      const index = this.todos.findIndex(x => x._id === id);
      this.todos.splice(index, 1);
    },
    getTodos: async function() {
      const todos = await Api().get(`todo`);
      console.dir(todos);
      todos.data.forEach(element => {
        this.todos.push(element);
      });
    }
  }
};
</script>

<style>
html,
body,
pre,
code,
kbd,
samp {
  font-family: "Press Start 2P";
}

body {
  background: #3273c9;
  padding: 20px;
}

#app {
  background: #fff;
  border-radius: 4px;
  padding: 20px;
  transition: all 0.2s;
}

li {
  margin: 8px 0;
}

del {
  color: rgba(255,0,0,0.3);
}

.padding {
  padding: 1px 7px 2px;
}

.flex {
  display: flex;
}

.space {
  flex-grow: 1;
}

.Add {
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}

.delete {background-color: #f44336;} /* Red */


</style>

