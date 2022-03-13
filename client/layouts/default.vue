<template>
  <v-app>
    <v-navigation-drawer>
    </v-navigation-drawer>
    <v-app-bar app>
    </v-app-bar>
    <v-main app>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
    <v-footer app>
      <v-row>
        <v-col align="center">
          <span>
              &copy; 2022～ M.Hirota
          </span>
        </v-col>
      </v-row>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data () {
    return {

    }
  }
}
</script>
