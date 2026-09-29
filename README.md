# SunnyJoshi Skills

Practical AI skills by Sunny Joshi. The first skill is **SunnyJoshi Humanizer**, a voice-preserving editor with support for natural Indian English and opt-in language mixing.

## Humanizer

Humanizer rewrites stiff or AI-sounding prose without changing its meaning. It:

- returns only the finished rewrite by default;
- preserves facts, intent, certainty, and calls to action;
- infers the audience, channel, and formality;
- matches a supplied writing sample;
- never uses em dashes in rewritten prose;
- supports neutral Indian English, Hinglish, and other regional language mixes without stereotyping.

### Install as an Agent Skill

```sh
npx skills add https://github.com/sj9911/sunnyjoshi-skills --skill humanizer
```

### Install in Claude Code

```text
/plugin marketplace add sj9911/sunnyjoshi-skills
/plugin install sunnyjoshi-skills@sunnyjoshi-skills
```

Then use:

```text
/sunnyjoshi-skills:humanizer

[paste your text]
```

You can also ask naturally:

```text
Rewrite this in my voice for an Indian LinkedIn audience: [text]
```

## Development

Run the package checks with:

```sh
python3 scripts/validate.py
```

## Credits

The Humanizer skill adapts ideas from [blader/humanizer](https://github.com/blader/humanizer), created by Siqi Chen and released under the MIT License. Its pattern catalogue also draws on Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).

## License

MIT
