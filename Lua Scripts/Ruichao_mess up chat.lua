local mt = getrawmetatable(game)
make_writeable(mt)
local old = mt.__namecall

mt.__namecall = newcclosure(function(self,...)
   local args  = {...}
   local m = getnamecallmethod()
   if tostring(m) == "FireServer" and self.Name == "SayMessageRequest" then
local output = args[1]
output = output:gsub("l", "")
output = output:gsub("L", "")
output = output:gsub("p", "")
output = output:gsub("P", "")
output = output:gsub("r", "")
output = output:gsub("R", "")
return old(self,output, args[2])
   end
   return old(self,...)
end)