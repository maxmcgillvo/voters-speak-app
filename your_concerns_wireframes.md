# Your Concerns Feature - Wireframes

## Desktop Layout

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│  YOUR CONCERNS                                                          │
│  Your voice matters in our democracy                                    │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  WHAT'S HAPPENING RIGHT NOW                                             │
│  Stay informed with coverage from multiple perspectives                 │
│                                                                         │
│  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐ │
│  │ CNN │  │ FOX │  │ NPR │  │ BBC │  │  AP │  │ NBC │  │HUFF │  │MORE │ │
│  │NEWS │  │NEWS │  │NEWS │  │NEWS │  │NEWS │  │NEWS │  │POST │  │  ▼  │ │
│  └─────┘  └─────┘  └─────┘  └─────┘  └─────┘  └─────┘  └─────┘  └─────┘ │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌───────────────────────┐  ┌───────────────────────┐  ┌───────────────┐│
│  │                       │  │                       │  │               ││
│  │  EPSTEIN FILES        │  │  FIRST AMENDMENT      │  │  ECONOMIC     ││
│  │  Should they be       │  │  Speak up, Be heard   │  │  ISSUES       ││
│  │  released?            │  │                       │  │               ││
│  │                       │  │  [Description text    │  │  [Description ││
│  │  [Description text    │  │   that spans 2-3      │  │   text...]    ││
│  │   that spans 2-3      │  │   sentences...]       │  │               ││
│  │   sentences...]       │  │                       │  │               ││
│  │                       │  │                       │  │               ││
│  │  [CONTACT OFFICIALS]  │  │  [CONTACT OFFICIALS]  │  │  [CONTACT...] ││
│  │                       │  │                       │  │               ││
│  └───────────────────────┘  └───────────────────────┘  └───────────────┘│
│                                                                         │
│  ┌───────────────────────┐  ┌───────────────────────┐  ┌───────────────┐│
│  │                       │  │                       │  │               ││
│  │  HEALTHCARE           │  │  IMMIGRATION &        │  │  SUPREME      ││
│  │  Costs, Coverage,     │  │  BORDER               │  │  COURT TERM   ││
│  │  Care                 │  │                       │  │               ││
│  │                       │  │  [Description text    │  │  [Description ││
│  │  [Description text    │  │   that spans 2-3      │  │   text with   ││
│  │   that spans 2-3      │  │   sentences...]       │  │   rotating    ││
│  │   sentences...]       │  │                       │  │   content]    ││
│  │                       │  │                       │  │               ││
│  │  [CONTACT OFFICIALS]  │  │  [CONTACT OFFICIALS]  │  │  [CONTACT...] ││
│  │                       │  │                       │  │               ││
│  └───────────────────────┘  └───────────────────────┘  └───────────────┘│
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

## Mobile Layout

```
┌───────────────────────────┐
│                           │
│ YOUR CONCERNS             │
│ Your voice matters        │
│                           │
├───────────────────────────┤
│                           │
│ WHAT'S HAPPENING RIGHT NOW│
│                           │
│ ┌─────┐ ┌─────┐ ┌─────┐  │
│ │ CNN │ │ FOX │ │ NPR │  │
│ │NEWS │ │NEWS │ │NEWS │  │
│ └─────┘ └─────┘ └─────┘  │
│                           │
│       < 1/3 >            │
│                           │
├───────────────────────────┤
│                           │
│ ┌─────────────────────┐   │
│ │                     │   │
│ │ EPSTEIN FILES       │   │
│ │ Should they be      │   │
│ │ released?           │   │
│ │                     │   │
│ │ [Description text]  │   │
│ │                     │   │
│ │ [CONTACT OFFICIALS] │   │
│ │                     │   │
│ └─────────────────────┘   │
│                           │
│ ┌─────────────────────┐   │
│ │                     │   │
│ │ FIRST AMENDMENT     │   │
│ │ Speak up, Be heard  │   │
│ │                     │   │
│ │ [Description text]  │   │
│ │                     │   │
│ │ [CONTACT OFFICIALS] │   │
│ │                     │   │
│ └─────────────────────┘   │
│                           │
│ ┌─────────────────────┐   │
│ │                     │   │
│ │ ECONOMIC ISSUES     │   │
│ │ Inflation, Housing  │   │
│ │                     │   │
│ │ [Description text]  │   │
│ │                     │   │
│ │ [CONTACT OFFICIALS] │   │
│ │                     │   │
│ └─────────────────────┘   │
│                           │
│         (etc.)            │
│                           │
└───────────────────────────┘
```

## News Source Component

### Desktop Version
```
┌─────────────────────────────────────────────────────────────────────────┐
│ WHAT'S HAPPENING RIGHT NOW                                              │
│ Stay informed with coverage from multiple perspectives                  │
│                                                                         │
│ ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐  │
│ │     │  │     │  │     │  │     │  │     │  │     │  │     │  │     │  │
│ │ CNN │  │ FOX │  │ NPR │  │ BBC │  │  AP │  │ NBC │  │HUFF │  │DAILY│  │
│ │NEWS │  │NEWS │  │NEWS │  │NEWS │  │NEWS │  │NEWS │  │POST │  │BEAST│  │
│ │     │  │     │  │     │  │     │  │     │  │     │  │     │  │     │  │
│ └─────┘  └─────┘  └─────┘  └─────┘  └─────┘  └─────┘  └─────┘  └─────┘  │
│                                                                         │
│ ┌──────────┐  ┌──────────┐                                              │
│ │          │  │          │                                              │
│ │BLOOMBERG │  │ GOOGLE   │                                              │
│ │  NEWS    │  │  NEWS    │                                              │
│ │          │  │          │                                              │
│ └──────────┘  └──────────┘                                              │
└─────────────────────────────────────────────────────────────────────────┘
```

### Mobile Version (Carousel)
```
┌───────────────────────────┐
│                           │
│ WHAT'S HAPPENING RIGHT NOW│
│                           │
│ ┌─────┐ ┌─────┐ ┌─────┐  │
│ │     │ │     │ │     │  │
│ │ CNN │ │ FOX │ │ NPR │  │
│ │NEWS │ │NEWS │ │NEWS │  │
│ │     │ │     │ │     │  │
│ └─────┘ └─────┘ └─────┘  │
│                           │
│       < 1/4 >            │
│                           │
└───────────────────────────┘
```

## Concern Card Component

### Desktop Version
```
┌───────────────────────────────────────────┐
│                                           │
│  EPSTEIN FILES                            │
│  Should they be released?                 │
│                                           │
│  The debate around transparency vs.       │
│  privacy continues as courts consider     │
│  releasing sealed documents related to    │
│  Jeffrey Epstein.                         │
│                                           │
│  ┌─────────────────────────────────────┐  │
│  │         CONTACT OFFICIALS           │  │
│  └─────────────────────────────────────┘  │
│                                           │
└───────────────────────────────────────────┘
```

### Mobile Version
```
┌─────────────────────────┐
│                         │
│ EPSTEIN FILES           │
│ Should they be released?│
│                         │
│ The debate around       │
│ transparency vs.        │
│ privacy continues as    │
│ courts consider         │
│ releasing sealed        │
│ documents.              │
│                         │
│ ┌───────────────────┐   │
│ │  CONTACT OFFICIALS│   │
│ └───────────────────┘   │
│                         │
└─────────────────────────┘
```

## Contact Officials Button

```
┌─────────────────────────────────────┐
│         CONTACT OFFICIALS           │
└─────────────────────────────────────┘
```

When clicked, this button should:
1. Link to a filtered view of officials relevant to the concern
2. Pass the list of official IDs as a parameter
3. Show a loading state while data is being fetched

## Design Notes

### Colors
- Use the existing color scheme from the Voters Speak application
- Consider using subtle accent colors for different concern categories
- Ensure sufficient contrast for accessibility

### Typography
- Use the existing font hierarchy from the Voters Speak application
- Title: Larger, bolder font
- Subtitle: Medium size, possibly italicized
- Description: Regular body text
- Button: Bold, clear call to action

### Spacing
- Consistent padding within cards (20px recommended)
- Equal spacing between cards (16-24px recommended)
- Responsive margins that adjust based on screen size

### Accessibility
- Ensure all text meets WCAG 2.1 contrast requirements
- Use proper heading hierarchy (h1, h2, h3, etc.)
- Include focus states for keyboard navigation
- Add appropriate ARIA labels for screen readers