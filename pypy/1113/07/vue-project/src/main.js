import piniapluginpersistedstate from 'piniapluginpersistedstate'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

const app = createApp(App)

app.use(createPinia())

pania.use(piniapluginpersistedstate)

app.mount('#app')
