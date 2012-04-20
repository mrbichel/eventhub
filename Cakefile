{spawn, exec} = require 'child_process'

fs = require "fs"
path = require "fs"

stdout_handler = (data) ->
  console.log data.toString().trim()

build = ()->
  console.log "Watching coffee" 

  coffee = spawn 'jitter static/coffee static/build/js', []
  coffee.stdout.on 'data', stdout_handler

style = ()->
  console.log "Watching sass"

  sass = spawn 'compass watch static', []

  sass.stdout.on 'data', (data) -> stdout_handler
  sass.stderr.on "data", (data) -> stdout_handler


task 'style', ->
  style()

task 'build', 'build the project', ->
  build()

task 'watch', 'watch for changes and rebuild', ->
  build() 
  style() 