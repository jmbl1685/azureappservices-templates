'use strict'

const express = require('express')
const app = express()

app.set('port', process.env.PORT || 3000)

app.get('/', (req,res) => {
  res.status(200).send({
    status: `Project running in Azure App Services`
  })
})

app.listen(app.get('port'), () => {
  console.log('Server running')
})