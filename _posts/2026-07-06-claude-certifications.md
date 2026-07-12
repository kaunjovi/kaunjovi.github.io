https://claude.com/resources/courses

[Go deeper with Anthropic courses](https://claude.com/resources/courses)

[Anthropic skilljar](https://anthropic.skilljar.com/)

[Course : Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action)


[Certification : Architect foundation](https://anthropic-partners.skilljar.com/claude-certified-architect-foundations-certification) 

1. List of pre-read. Free. 
   1. https://anthropic-partners.skilljar.com/ai-fluency-framework-foundations 
   2. https://anthropic-partners.skilljar.com/claude-with-the-anthropic-api
   3. https://anthropic-partners.skilljar.com/claude-with-google-vertex
   4. https://anthropic-partners.skilljar.com/claude-101
   5. https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock
   6. https://anthropic-partners.skilljar.com/introduction-to-model-context-protocol
   7. https://anthropic-partners.skilljar.com/claude-code-in-action
   

[Course : Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action)

1. **/init** - read about the code. Write notes in the CLAUDE.md. 
1. Shift Tab - auto accept all changes. 
1. Every request that you make to claude, contains the content of the file CLAUDE.MD 
1. You can update claude.md file to give claude some general guidance. 
   1. **CLAUDE.md** - generated with /init. commit to git and shared. 
   2. **CLAUDE.local.md** - do not check in. your personal commands etc. 
   3. **~/.claude/CLAUDE.md** - in your machine. instructions for all projects in your machine. 
2. How to update the CLAUDE.md to change some behaviour e.g. write less comments. 
3. 1. "# use comments sparingly." 
4. Or ask claude some question about the code 
5. "> How does auth system work?" 
6. "> How does auth system work? @name-of-the-file @name-of-the-file-1" 

## How do you provide a image to claude code? 
1. Ctrl V. Even in mac. 

## How to optimize for more reasearch when the code ask needs deeper read ? 
1. Go to plan mode. shift tab , shift tab or /plan 
2. You are going for breadth 

## How hard is claude thinking? 
1. Want to see claudes thinking process ? ctrl 0 
2. How hard is it thinking? /effort 
3. Boost up the thinking ? /ultrathink 
4. You are going for depth. 

## TIP : Rewind a conversation  
1. If you have given a task - write tests. 
2. You see that during the process, it had to take a detour - e.g. to debug and fix some issues. 
3. There is a lot of additional information now about the debugging that is not really required for the original task. 
4. Escape, Escape - go back in the conversation.    

## Controlling context 
1. Interrup? **Esc**
2. Long task. Took detour. Have some info now that is not required. Go back in the conversation. **Escape Escape**
3. Long task. Useful context. But voluminous. ? **/compact**
4. Too much conversation. Start over ? **/clear** 

## List of helpful commands 

1. Show list of commands. **/**
1. Interrup? **Esc**
2. Long task. Took detour. Have some info now that is not required. Go back in the conversation. **Escape Escape**
3.  Long task. Useful context. But voluminous. ? **/compact**
4.  Too much conversation. Start over ? **/clear** 


## Add your own command 
1. **.claude/commands/my-own-command.md** - It is an md file. Provide a blue print of what you are trying to do. 
   
## MCP server 

## Hooks 
1. Run code before / after a code is run. e.g. code formatter. 
2. **PreToolUse** or **PostToolUse** hooks. They go in **settings.local.json**
3. You can use this to figure out what Claude wants to do it and if you want to block it, you are free to do so. 
4. Stop Claude from ever readign the .env file, since it may contain secret keys. 
   1. This has to be a PreToolUse hook. 
   2. But which tool. There are so many. And we can use custom tools also. 
   3. :( you ask claude to list the tools that it has access to and based on that work 
   4. but, that is a point in time. What happens if new tool was added later. 
   5. Exit 2, if the tool call was blocked. Also Stderr logs sent to claude. 



