<template>
  <div>
    <div>
      <h3>Subir varios - con varios campos de input</h3>
    </div>
    <div>
      <button @click="agregarArchivo">Nuevo Archivo</button>
    </div>
    <div>{{ this.selectedFiles }}</div>
    <div>
      <ul>
        <li v-for="(file, index) in selectedFiles" :key="index">
          {{ index }}
          <input type="file" @change="onFileSelected($event, index)" />
        </li>
      </ul>
    </div>
    <div>
        <button @click="onUpload">Upload</button>
    </div>
  </div>
</template>

<script>
// yarn add axios
import axios from "axios";

export default {
  data() {
    return {
      selectedFiles: [],
      file: null
    };
  },
  methods: {
      agregarArchivo() {
        this.selectedFiles.push(this.file);
      },
    onFileSelected(event, index) {
      this.selectedFiles[index] = event.target.files[0];
      console.log(this.selectedFiles);
    },
    onUpload() {
      if (!this.selectedFiles) {
        alert("Por favor elija un archivo");
        return;
      }

      const fd = new FormData();
      let file;

      for (let i = 0; i < this.selectedFiles.length; i++) {
        file = this.selectedFiles[i];
        fd.append("files", file);
      }

      axios
        .post("http://127.0.0.1:8000/upload/files", fd, {
          onUploadProgress: (uploadEvent) => {
            console.log(
              `Upload progress: ${Math.round(
                (uploadEvent.loaded / uploadEvent.total) * 100
              )} %`
            );
          },
        })
        .then((res) => {
          console.log(res);
          alert(JSON.parse(res.data).message);
        })
        .catch((res) => {
          alert("Hubo un error en la carga de los archivos");
        });
    },
  },
};
</script>

<style>
</style>