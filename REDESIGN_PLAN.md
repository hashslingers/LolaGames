# 🦋 THE GRAVITY OF LOLA
## Complete Vision Document — All Questions Answered

**Audience:** Lola, age 6.5 · Solo first, then parent co-op for future stages
**Device:** Tablet (touch-first design)
**Character Sprite:** `Lola-bit.png` (1920×2194px)
**Engine:** Single-file HTML5 Canvas
**Date:** April 11, 2026

---

> *"The best games are the ones where the mechanic teaches you something you already knew but had not yet articulated."*
> — Tomorrow, and Tomorrow, and Tomorrow

---

## THE STORY — Lola Is the Princess

This is the heart of everything.

Lola sets out to rescue the princess trapped in the Upside-Down Castle. She fights through the Butterfly Kingdom, flips gravity, outwits a ridiculous villain, collects butterflies, and finally reaches the highest tower.

She opens the door.

There is a mirror.

**The princess is Lola.**

The message written across the five rooms — revealed letter by letter, each one only readable from a different gravitational orientation — was always for her:

> **YOU ARE SO AMAZING.**

She didn't need to rescue anyone. She just needed to see herself clearly. And to do that, she had to learn to see the world from every angle first.

---

### Why This Story Works for a Shy 6.5-Year-Old

The game says her name out loud when she does something brave. It throws confetti when she collects a star. The villain falls on his face. The butterflies follow her everywhere. Every moment of the game is designed to make her feel what the ending screen tells her explicitly:

*You were the hero all along. You were the amazing one. You.*

For a child working through shyness, this is not just entertainment. It is a small, private mirror held up with love.

---

## THE VILLAIN — Lord Flopp

*(A Buffoonish Darth Vader)*

Lord Flopp is tall, wears a magnificent dark cape, has a deep dramatic voice — and absolutely cannot get anything right.

He trips over his cape constantly. When he tries to flip gravity himself, he ends up stuck to the ceiling, cape over his face, legs dangling. His dramatic monologues get interrupted by him accidentally bonking his head on doorframes. His henchmen are butterflies who don't take him seriously at all.

He is not scary. He is the funniest thing in the game. A 6.5-year-old should laugh every single time he appears.

**His design:**
- Tall, dark silhouette (big cape, pointy hat)
- Bright round eyes that go wide when he's confused
- Falls in slow-motion when he trips, arms windmilling
- His "evil laugh" keeps turning into hiccups
- When Lola flips gravity near him, he tumbles helplessly upward, shouting *"NOT AGAIN!"*
- He is defeated not by being hit — but by Lola flipping gravity so many times that he gets completely dizzy and sits down

**His role in the story:** Lord Flopp stole the Gravity Crystals from the Butterfly Kingdom, causing gravity to go haywire. He didn't mean to break everything — he just wanted to be impressive. He's not evil. He's embarrassing.

At the end, when Lola reaches the mirror and sees herself, Lord Flopp peeks in from around the corner — and for a moment, looks genuinely moved. *"Oh,"* he says quietly. *"You really are amazing."* Then he trips over his cape and falls off screen.

---

## THE MECHANIC — Gravity, For a 6.5-Year-Old

### The One Rule
**Tap the big butterfly button → gravity flips.**

That's it. That's the whole mechanic.

- Tap it once: Lola falls upward. The ceiling is now the floor.
- Tap it again: Lola falls downward. The floor is back.
- Jump button: always jumps away from the current surface (floor or ceiling)

No combinations. No timing windows. No second-guessing.

### The Feeling
When Lola flips gravity:
- Her hair swooshes upward (or downward)
- A burst of butterflies scatters from her body
- The game says her name: **"LOLA!"** — bright, warm, celebratory
- A gentle *whooomp* sound plays, like turning a world upside down
- Flower petals and sparkles drift in the new direction of "down"
- She grins — the Run or Jump animation carries extra joy

This is not a puzzle tool. This is a **delight machine.** She will tap it 50 times just because it feels wonderful.

### Float Mechanic
If she holds the gravity button in mid-air, Lola briefly floats — butterfly wings appear from her back, she hovers for 2 seconds. This is the *safety net* for a 6.5-year-old. If she overshoots a platform, she can float down gently. No frustration.

### The Voice System — Saying Lola's Name
The game uses Web Speech API to speak her name at key moments:

| Moment | Voice Line | Tone |
|--------|-----------|------|
| First gravity flip | *"Lola!"* | Delighted surprise |
| Collecting a star | *"Yay, Lola!"* | Pure joy |
| Completing a room | *"Amazing, Lola!"* | Warm, proud |
| Taking a hit | *"You've got this, Lola!"* | Encouraging, gentle |
| Gravity slam | *"Whoa, Lola!"* | Impressed |
| Final mirror moment | *"Lola... that's you."* | Soft, wonder |

This is therapeutic game design. A shy child hearing her own name celebrated, again and again, associated with power and success — that is a gift.

---

## TABLET CONTROLS — Touch-First Layout

```
┌─────────────────────────────────────────────┐
│                                             │
│           🎮 GAME SCREEN                   │
│                                             │
│                                             │
│                                             │
│                                             │
├────────────┬──────────────┬────────────────┤
│            │              │                │
│  ◄  ►      │   🦋 FLIP    │    ⬆ JUMP      │
│  (move)    │  (gravity)   │               │
│            │              │                │
└────────────┴──────────────┴────────────────┘
```

- **Left zone (large):** Virtual D-pad or left/right arrows — move Lola
- **Center button (largest, most beautiful):** Big glowing butterfly — FLIP GRAVITY
  - This is the hero button. It should be irresistible to tap.
  - Pulses gently. Butterflies orbit it.
- **Right button:** Jump
- **All buttons:** Large, forgiving touch targets (minimum 80px)
- **No accidental triggers:** 100ms debounce on gravity flip

---

## THE WORLD — Five Zones + The Castle

Each zone is short (60–90 seconds), bright, and ends with a clear celebration before the next begins. Solo play = one zone at a time. Parent co-op stages (future) = zones that need two-player gravity cooperation.

### Zone 1: 🌿 The Sunny Meadow *(Gravity Tutorial)*
Normal gravity. Lola runs right, meets butterflies. Lord Flopp appears dramatically, trips immediately, accidentally knocks a Gravity Crystal into the sky. The world tilts. The game asks Lola to flip gravity for the first time.

**This zone teaches:** Left, right, jump, and the first gravity flip. Nothing else.

**Lord Flopp cameo:** He's stuck on the ceiling in the background, kicking his legs. Can't get down.

---

### Zone 2: 🌑 The Upside-Down Garden *(Ceiling Walking)*
Gravity is reversed. Flowers grow downward from above (which is now the floor). Giant friendly snails wander the ceiling (also reversed). Lord Flopp runs past in the background, still trying to figure out which way is up.

**This zone teaches:** The ceiling is now the floor. Everything familiar looks different from here.

**Discovery:** A new flower species only visible from upside-down. It makes Lola sneeze butterflies.

---

### Zone 3: 🌊 The Bubble River *(Floating + Switching)*
A water zone. Gravity bubbles rise up AND fall down — Lola must flip gravity to ride them. Lord Flopp is in a little boat that keeps flipping over.

**This zone teaches:** Switching gravity mid-air. Using the float to land on moving surfaces.

**Secret:** Axolotls live here. They wave at Lola and blow bubbles shaped like stars.

---

### Zone 4: 🌈 The Rainbow Pass *(Speed + Joy)*
Fast horizontal run. Rainbow-colored platforms at different heights, reachable only by flipping. This is the "feels amazing" zone — pure speed, music picks up, everything sparkles. Lord Flopp tries to follow on a unicycle and immediately crashes.

**This zone teaches:** Nothing new — this is the *reward* zone where everything she's learned clicks into pure flow.

---

### Zone 5: 🏰 The Upside-Down Castle *(Five Rooms)*
See room breakdown below.

---

## THE FIVE CASTLE ROOMS — Full Design

### Room 1: The Rainbow Hall
**Goal:** Collect 5 glowing stars
**Gravity use:** Stars on floor AND ceiling — must flip to reach both
**How it teaches:** Stars pulse and float toward Lola slightly (very forgiving). She can't miss.
**Voice:** *"One more, Lola!"* when she has 4 stars
**Hidden letter:** `Y` — glows on the ceiling, only visible after flipping

---

### Room 2: The Unicorn Stable
**Goal:** Find the unicorn facing the other way
**Gravity use:** One unicorn faces "differently" — but from the ceiling, it's even more obvious. Flipping gravity makes the answer jump out.
**Simplification for 6.5:** The "different" unicorn has a big golden glow around it — she just needs to reach it. The gravity flip reveals it clearly.
**Lord Flopp cameo:** He's in a stall, wearing a unicorn horn, hoping no one notices.
**Hidden letter:** `O` — painted on the back wall, readable right-side-up

---

### Room 3: The Axolotl Pond
**Goal:** Catch 5 friendly axolotls
**Gravity use:** Some axolotls swim near the ceiling, some near the floor — flip to reach them
**Design:** Axolotls are irresistible. Pink, big eyes, they squeak adorably when caught and give Lola a tiny hug animation.
**Voice:** *"Lola found a friend!"* on first catch
**Hidden letters:** `A` and `R` — reflected in the water

---

### Room 4: The Butterfly Garden *(Memory Game)*
**Goal:** Match 4 pairs of butterfly cards
**Gravity use:** One pair is on the floor, its match is on the ceiling — must flip to find it
**Simplification for 6.5:** Cards stay face-up for 4 seconds (double the current 40-frame lock). Only 4 pairs, not more. Cards are large and colorful.
**Secret delight:** When a pair is matched, two butterflies fly out and dance around Lola
**Hidden letter:** `E` — appears between the dancing butterflies when a pair matches

---

### Room 5: The Throne Room *(The Mirror)*
**Goal:** Reach the throne
**Gravity use:** The path to the throne zigzags between floor and ceiling — Lola must flip 3 times
**The reveal:** She reaches the throne. Lord Flopp appears at the door dramatically: *"Ah-ha! Now I have you—"* trips, crashes into the wall, accidentally knocks over the mirror covering the throne.

Lola sees herself.

The screen fills gently with gold light. All five clue words light up simultaneously:

> ✨ **YOU ARE SO AMAZING** ✨

The voice says softly: *"Lola... that's you."*

Butterflies fill the screen. The music swells. Lord Flopp peeks around the corner, sniffles, and quietly places a tiny crown on the floor before tiptoeing away.

**Hidden letter:** `!` — forms from the butterflies themselves

---

## MUSIC & AUDIO DESIGN

**Philosophy:** Light, warm, gentle. A lullaby that keeps its energy. Think: xylophone melodies, soft bells, rounded bass notes. The kind of music a parent hears from the next room and feels calm, not irritated. The kind a child hums afterward without knowing it.

| Zone | Music Character | Tempo |
|------|----------------|-------|
| Meadow | Cheerful, skipping xylophone | Medium |
| Upside-Down Garden | Same melody, gently inverted/mirrored | Medium |
| Bubble River | Watery, bubbling, playful | Gentle |
| Rainbow Pass | Bright, fast, triumphant | Upbeat |
| Castle | Warm, slightly mysterious, still safe | Slow-medium |
| Mirror Moment | Single held note → gentle swell | Still |
| Victory | Full bright fanfare, then the lullaby returns | Joyful |

**Sound effects — all warm and rounded:**
- Gravity flip: a soft *whooomp* + shimmer
- Jump: a light *boing*
- Star collect: a xylophone ping
- Lord Flopp falling: a cartoon *BWONG* + slide whistle
- Axolotl catch: a tiny happy squeak
- Voice lines: warm, female or neutral voice, reads like a proud teacher

---

## ENEMY & OBSTACLE DESIGN — Nobody Gets Hurt

At 6.5, enemies are **comic obstacles**, not threats.

| Creature | Behavior | What Happens on Contact |
|---------|----------|------------------------|
| **Bumble Puffs** | Float randomly | They bounce off Lola and spin away with a squeak. Lola giggles (animation). |
| **Ceiling Worms** | Inch along ceiling | Walk away from Lola. She needs to flip to get past them. They wave politely. |
| **Stone Butterflies** | Pull Lola slightly off course | Lola can tap them to make them crumble into sparkles |
| **Lord Flopp** | Appears, trips, leaves | Pure comedy. Never actually blocks Lola. Always falls. |

**On any collision:** Lola plays her Hit animation (brief wince), bounces back two steps, sparkles appear, voice says *"You've got this, Lola!"* — and she's immediately fine. No health bar. No game over. Just a gentle nudge and an encouraging voice.

---

## VISUAL IDENTITY

**Palette:** Warm pastel primaries. Sky blue, meadow green, sunshine yellow, soft pink. Saturated enough to feel joyful, soft enough to feel safe.

**Lola renders:** From `Lola-bit.png` sprite sheet — chibi proportions, brown hair, blue sweater. She is already perfect. She just needs to be big and clear on screen.

**Butterfly design:** Round, friendly, slightly too big for a real butterfly. They leave trails of golden sparkles. They follow Lola at a gentle distance. When gravity flips, they scatter and slowly regroup. They are always, always smiling.

**Lord Flopp design:** Tall dark silhouette, enormous round eyes, cape that has a life of its own (keeps wrapping around his face at the worst moments). His expressions are enormous and readable from a distance.

**UI principles:**
- No health bar — just a floating row of 3 heart butterflies (wings fold if hit, reopen after 3 seconds)
- Gravity indicator: a friendly butterfly in the corner — always pointing "down," rotates when gravity flips
- Progress: 5 glowing castle windows across the top — each lights up when a room is complete
- All text: rounded, large, friendly font — used sparingly

---

## MISSING SPRITE ANIMATION — PRIORITY REQUEST

**The gravity-flip frame is the most important new art asset.**

Without it: the gravity flip is a toggle.
With it: the gravity flip is *flying*.

**What to draw:** 1–2 frames of Lola mid-flip:
- Arms spread wide
- Hair streaming upward (or downward — mid-transition)
- Feet leaving the ground, toes pointed
- Expression: pure glee — wide eyes, open mouth, the best surprise
- Butterfly wings optional (can be added procedurally in code)

This is the frame she'll see 200 times per session. It is worth spending real time on.

---

## TECHNICAL PLAN — What Changes, What Stays

### What Stays (Reuse from existing 2,020-line game)
- Web Audio API procedural sound system (just add new sounds)
- World scenery drawing (sky, mountains, clouds, trees, castle exterior)
- Particle system (extended with butterfly burst + sparkle effects)
- Castle room puzzle logic (all 5 rooms, adapted)
- DOM UI structure (reskinned)
- Screen shake, transition effects
- Camera follow system

### What Gets Replaced
| Old | New |
|-----|-----|
| Butterfly physics (free-floating, no gravity) | Lola physics (real gravity, jump, gravity flip toggle) |
| `drawButterfly()` procedural drawing | `drawLola()` sprite sheet rendering from `Lola-bit.png` |
| Keyboard-only input | Touch controls (tablet virtual buttons) |
| Lightsaber combat | Magic sparkle interaction (no combat) |
| Guard/boss enemies | Bumble Puffs, Ceiling Worms, Lord Flopp |
| Kills/combo counter HUD | Heart butterflies + gravity compass |

### New Systems to Build
- `gravityDir` variable (1 or -1), toggled by tap
- Ground + ceiling collision (Lola can stand on both)
- Platform geometry (the world can't just be one flat floor)
- Touch input mapping (left/right zones + jump + gravity buttons)
- Web Speech API voice system (`"Lola!"`)
- Gravity-flip visual effects (hair lag, butterfly burst, screen tilt)
- Float mechanic (hold gravity button mid-air)

---

## PHASE PLAN — BUILD ORDER

### ✅ Phase 0 — Foundation
Replace butterfly with Lola. Real gravity. Jump. Ground collision. Touch controls. Sprite rendering. Before any level design.

### ✅ Phase 1 — The Magic Button
Gravity flip works beautifully. The visual effects (butterflies, hair, sound, voice) are all in place. She can flip gravity 50 times just for fun and it never gets old.

### ✅ Phase 2 — Zone 1: Sunny Meadow
Just the tutorial zone. Stars to collect. First Lord Flopp appearance. Works fully on tablet. Ship this and watch Lola play it.

### ✅ Phase 3 — The Castle
All five rooms, adapted for a 6.5-year-old. The mirror reveal. The voice moment. The ending.

### ✅ Phase 4 — Remaining Zones (2–4)
Zones 2, 3, and 4 connecting the meadow to the castle. Lord Flopp cameos throughout.

### ✅ Phase 5 — Parent Co-op (Future)
New levels designed for two players — one controls Lola, one controls gravity. Designed for a parent sitting beside their child, making it together.

---

## THE ENDING — Written Out

*Lord Flopp stumbles out of frame. The mirror glows.*

*Lola stands alone, looking at herself.*

*The five letters light up one by one:*

**Y — O — U**

*The voice says her name, softly.*

**A — R — E**

*Butterflies drift across the screen.*

**S — O — A — M — A — Z — I — N — G**

*Then, warmly, the voice:*

*"Lola... that's you."*

*Confetti. Her Win animation — that big, genuine smile.*

*And the butterflies, all of them, land on the word* AMAZING *and hold still.*

---

*All questions answered. Ready to build.*
*— April 11, 2026*
