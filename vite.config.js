import { defineConfig } from 'vite'
import { viteStaticCopy } from 'vite-plugin-static-copy'

export default defineConfig({
  plugins: [
    viteStaticCopy({
      targets: [
        {
          src: 'src/assets/favicon/*',
          dest: '',
        },
      ],
    }),
  ],
  build: {
    outDir: 'static',
    assetsDir: '',
    rollupOptions: {
      input: {
        main: './src/app/core/client/main.ts',
        hello: './src/app/features/hello/client/main.ts',
      },
      output: {
        entryFileNames: '[name].js',
        chunkFileNames: '[name].js',
        assetFileNames: '[name].[ext]',
      },
    },
  },
})
